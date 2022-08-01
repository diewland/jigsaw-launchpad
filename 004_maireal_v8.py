import json
 
TOKEN_SIZE = 20
START_ID = 160

NAME = "Mai-Real v8"
DESC = "Discover founder secret weapon."
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/maireal_unreveal.png"
ATTRS = [
    # standard
    {
      "trait_type": "Collection",
      "value": NAME, 
    },
    # custom
    {
      "trait_type": "Rarity",
      "value": "Unrevealed",
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
    tpl["name"] = "Mai-Real #{}".format(id)
    #tpl["name"] = "{} #{}".format(NAME, id)
    with open("./004_maireal_v8/{}".format(START_ID + id), "w") as f:
        json.dump(tpl, f)
