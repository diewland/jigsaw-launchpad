import json
 
TOKEN_SIZE = 145
START_ID = 0
OUTPUT_DIR = '010_lego_dragon'

NAME = "LegoDragon"
DESC = "LegoDragon 145 Dragons can be fly, They will coming with 7Angles or 7Devils. Dragon born to be a Whitelist to next collection. Reval in 5 day"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/lego-dragon/LegoDragon%23{}.png" # 0-144
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

tpl = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    tpl["name"] = "{} #{}".format(NAME, id)
    tpl["image"] = IMG.format(id)
    with open("./{}/{}.json".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(tpl, f)
