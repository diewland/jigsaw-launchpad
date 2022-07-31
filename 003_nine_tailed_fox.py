import json
 
TOKEN_SIZE = 1
START_ID = 159

NAME = "Nine-Tailed Fox"
DESC = "Collect 9 Nine-Tailed Fox Tails to summon Nine-Tailed Fox"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/nine_tailed_fox_signed.png"
ATTRS = [
    # standard
    {
      "trait_type": "Collection",
      "value": "Nine-Tailed Fox", 
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
    tpl["name"] = NAME #"{} #{}".format(NAME, id+1)
    with open("./003_nine_tailed_fox/{}".format(START_ID + id), "w") as f:
        json.dump(tpl, f)
