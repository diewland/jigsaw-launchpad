import json
 
TOKEN_SIZE = 9
START_ID = 150

NAME = "Nine-Tailed Fox Tail"
DESC = "Collect 9 Nine-Tailed Fox Tails to summon Nine-Tailed Fox"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/nine_tailed_fox_tail.png"
ATTRS = [
    # standard
    {
      "trait_type": "Collection",
      "value": "Nine-Tailed Fox", 
    },
    # custom
    {
      "trait_type": "Rarity",
      "value": "Super Rare",
    },
]
ENGINE = "Jigsaw Engine"

tpl = {
  "name": "<FILL-IN-LOOP>",
  "description": DESC,
  "image": IMG,
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    tpl["name"] = "{} #{}".format(NAME, id+1)
    with open("./003_nine_tailed_fox/{}".format(START_ID + id), "w") as f:
        json.dump(tpl, f)
