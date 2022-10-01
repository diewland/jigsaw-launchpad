import json
 
TOKEN_SIZE = 300
START_ID = 0
OUTPUT_DIR = '013_tama'

NAME = "Tama DOA"
DESC = "Better Call Tama! We're Tama. You're Tama. They're Tama.  Fast Work, Urgent Work, Say Tama! No Utility, No Road Map, No Art, Just Tama!"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/tama/tama%20({}).png" #1-300
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
