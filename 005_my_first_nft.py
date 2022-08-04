import json
 
TOKEN_SIZE = 20
START_ID = 180
OUTPUT_DIR = '005_my_first_nft'

NAME = "My First NFT Project"
DESC = "Publish your first NFT on Optimism Chain."
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/my-first-nft.png"
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
