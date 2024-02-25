from os import listdir, path
from json import load, dump

folder = './badges'
base_link = 'https://ziadoua.github.io/m3-Markdown-Badges/badges'

badge_list = sorted([badge for badge in listdir(folder) if path.isdir(path.join(folder, badge))], key=str.lower)

with open("badge_list.json", "r") as badge_list_json:
    data = load(badge_list_json)

data["badge_list"] = badge_list

with open("badge_list.json", "w") as badge_list_json:
    dump(data, badge_list_json, indent=4)

# README Generation

readme_template = open("./template/README.md", "r")
readme_template_data = readme_template.read()

generated_readme = open('./README.md', 'w')
generated_readme.write(readme_template_data)

generated_readme.close()
generated_readme = open('./README.md', 'r')

generated_readme_data = generated_readme.readlines()

for line in generated_readme_data:
    if line.strip() == '[M3-MATERIAL-BADGES:STATIC-BADGES-LIST]':
        generated_readme_data_top = generated_readme_data[:generated_readme_data.index(line)]
        generated_readme_data_bottom = generated_readme_data[generated_readme_data.index(line) + 1:]
        break

generated_readme.close()
generated_readme = open('./README.md', 'w')

generated_readme.writelines(generated_readme_data_top)

generated_readme.write(f'# Static Badges **[{len(badge_list)}]**\n')
generated_readme.write('| Badge | URL |\n| ------| --- |\n')

for folder_name in badge_list:
    for variant in range(3):
        generated_readme.write(f'| <img src="{base_link}/{folder_name}/{folder_name.lower()}{variant + 1}.svg"> | `{base_link}/{folder_name}/{folder_name.lower()}{variant + 1}.svg` |\n')

generated_readme.writelines(generated_readme_data_bottom)

generated_readme.close()
