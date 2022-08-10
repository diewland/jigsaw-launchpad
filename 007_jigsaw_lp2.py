import json
 
TOKEN_SIZE = 20
START_ID = 0
OUTPUT_DIR = '007_jigsaw_lp2'

NAME = "Thank you NFT"
DESC = "Thank you for using Jigsaw Launchpad."
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/jigsaw_lp_logo.gif"
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
