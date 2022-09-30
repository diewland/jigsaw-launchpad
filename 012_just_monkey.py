import json
 
TOKEN_SIZE = 1000
START_ID = 0
OUTPUT_DIR = '012_just_monkey'

NAME = "JustMonkey 🐵"
DESC = "No Utility No Roadmap No Reveal(Maybe)  Just Monkey 🐵 I love Banananana Uga Uga !!!"
IMG = "https://raw.githubusercontent.com/diewland/jigsaw-launchpad/master/assets/just-monkey/Monkey.gif"
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
    metadata["image"] = IMG#.format(id)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
