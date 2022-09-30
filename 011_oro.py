import json
 
TOKEN_SIZE = 300
START_ID = 0
OUTPUT_DIR = '011_oro'

NAME = "One Round 👁️nly"
DESC = 'The NFT will remind u to trust what you see you hv one round only to see through a truth. No roadmap, no utiltiy, no art, only Truth. 300/300 "Men trust their ears less than their eyes." Herodotus'
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/oro/One_Round_Only%20({}).png" # 1-300
ATTRS = [
    # standard
    #{
    #  "trait_type": "Collection",
    #  "value": NAME, 
    #},
    # custom
    #{
    #  "trait_type": "Rarity",
    #  "value": "Unrevealed",
    #},
]
ENGINE = "Jigsaw Engine"

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(id+1)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
