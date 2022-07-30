import json
 
NAME = "ApetiRun Founder"
DESC = "Got 500 score in ApetiRun before 2022/07/31 20:00 UTC+7"
IMG = "https://diewland.github.io/jigsaw-launchpad/assets/atr_founder.png"
ATTRS = [
    # standard
    {
      "trait_type": "Collection",
      "value": "ApetiRun", 
    },
    # custom
    {
      "trait_type": "Medal",
      "value": "Founder",
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

for id in range(0, 50): # 50-99
    tpl["name"] = "{} #{}".format(NAME, id)
    with open("./002_atr_founder/{}".format(id+50), "w") as f:
        json.dump(tpl, f)
