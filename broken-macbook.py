import json
 
TOKEN_SIZE = 20
START_ID = 221
OUTPUT_DIR = 'json_v1'

NAME = "The Beauty of Imperfection: A Look at the Elegance of a Broken MacBook Screen"
DESC = "The MacBook is a symbol of sleek design and cutting-edge technology, but what happens when the screen is shattered? Instead of viewing it as a failure, let's look at the aesthetic appeal of a broken MacBook screen. The cracks and shards of glass create a unique pattern, almost resembling a piece of modern art. It's a reminder that beauty can be found in the most unexpected places and that imperfections can add character and depth. The broken screen also serves as a metaphor for the fragility of technology and the fleeting nature of perfection. It's important to remember that just because something is broken, it doesn't mean it's worthless. A broken MacBook screen can still function, it's just a matter of finding a new way to look at it. So next time you come across a broken MacBook, take a moment to appreciate the unexpected beauty that it holds."
IMG = "https://raw.githubusercontent.com/diewland/jigsaw-launchpad/5311c9429e326e3ebef0d145e7990eb2aba17e0b/assets/FmW-iMuaYAM1XDj.jpeg"
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

metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, TOKEN_SIZE):
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    with open("./{}/{}".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)