import json
 
NAME = "Just Bananas"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/just_bananas.png"
ATTRS = [
    {
      "trait_type": "Collection",
      "value": NAME, 
    },
    {
      "trait_type": "Rarity",
      "value": "👀",
    },
]
ENGINE = "Jigsaw Engine"

tpl = {
  "name": "<FILL-IN-LOOP>",
  "description": NAME,
  "image": IMG,
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, 50): # 0-50
    tpl["name"] = "{} #{}".format(NAME, id)
    with open("./json/{}".format(id), "w") as f:
        json.dump(tpl, f)
