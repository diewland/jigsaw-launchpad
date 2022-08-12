import json
 
TOKEN_SIZE = 30
START_ID = 20
OUTPUT_DIR = '008_exclusive_artist'

NAME = "Exclusive Artist"
DESC = "Unrevealed"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/lock_500.png"
ATTRS = [
    # standard
    {
      "trait_type": "Collection",
      "value": NAME, 
    },
    # custom
    #{
    #  "trait_type": "Rarity",
    #  "value": "Unrevealed",
    #},
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
    tpl["name"] = "{} #{}".format(NAME, id)
    with open("./{}/{}".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(tpl, f)
