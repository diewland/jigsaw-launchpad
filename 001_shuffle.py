from pprint import pprint as pp
from random import shuffle
import json

# config
START_ID = 0
TOKEN_SIZE = 50
OUTPUT_PATH = '001_justbananas_revealed'
RARITY_COMMON = 'C'
RARITY_RARE = 'R'
RARITY_SUPER_RARE = 'S'
config = [
    (RARITY_COMMON, 44),
    (RARITY_RARE, 5),
    (RARITY_SUPER_RARE, 1),
]
rarity_map = {
    RARITY_COMMON: ('Common', 'Banana Flavored Milk', 'https://diewland.github.io/jigsaw-launchpad/assets/banana_flavored_milk.png'),
    RARITY_RARE: ('Rare', 'Chocholate Dipped Banana', 'https://diewland.github.io/jigsaw-launchpad/assets/choco_dipped_banana.png'),
    RARITY_SUPER_RARE: ('Super Rare', 'Banana Split', 'https://diewland.github.io/jigsaw-launchpad/assets/banana_split.png'),
}

# template
NAME = "Just Bananas"
ATTRS = [
    {
      "trait_type": "Collection",
      "value": NAME, 
    },
    {
      "trait_type": "Rarity",
      "value": "***",
    },
]
ENGINE = "Jigsaw Engine"
tpl = {
  "name": "***",
  "description": NAME,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

# prepare data
data = []
for c in config:
    data += c[0] * c[1]

# suffle 16 times
# round#16 result => CCCCCCCCCCCCRCCCCCSCCCRCCCCCCRCRCCCCCCCCCCCCCRCCCC
pattern = None
for rnd in range(0, 16):
    shuffle(data)
    pattern = ''.join(data)
    #print('round #{:02d} -> {}'.format(rnd, pattern))
print('round#16 result =>', pattern)

# render to files
num_c = 0
num_r = 0
num_s = 0
for id in range(0, TOKEN_SIZE):
    # get rarity
    code = pattern[id]
    (rarity, title, img) = rarity_map[code]
    # get running number
    if code == RARITY_COMMON:
        num = num_c
        num_c += 1
    elif code == RARITY_RARE:
        num = num_r
        num_r += 1
    elif code == RARITY_SUPER_RARE:
        num = num_s
        num_s += 1
    # update template
    tpl["name"] = "{} #{}".format(title, num)
    tpl["image"] = img
    tpl["attributes"][1]["value"] = rarity
    # write output file
    with open("./{}/{}".format(OUTPUT_PATH, START_ID + id), "w") as f:
        json.dump(tpl, f)
