from os import listdir, path
from json import load, dump

folder = './badges'

badge_list = [badge for badge in listdir(folder) if path.isdir(path.join(folder, badge))]

with open("badge_list.json", "r") as badge_list_json:
    data = load(badge_list_json)

data["badge_list"] = badge_list

with open("badge_list.json", "w") as badge_list_json:
    dump(data, badge_list_json, indent=4)