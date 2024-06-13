import yaml
import os
from pprint import pprint
from jinja2 import Environment, PackageLoader, select_autoescape

if __name__ == '__main__':

    try:
        with open('badges.yml', 'r') as yaml_file:
            badges = yaml.safe_load(yaml_file)
        with open('team.yml', 'r') as yaml_file:
            team = yaml.safe_load(yaml_file)
    except:
        exit("Error reading yml files")

    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape(),
        keep_trailing_newline=True
    )

    team.sort(key=lambda x: x['name'])

    template = env.get_template("team-member.md")
    try:
        os.unlink('output.md')
    except FileNotFoundError:
        pass
    with open('output.md', 'a') as output_file:
        for user in team:
            output_file.write(template.render(badges=badges, user=user))
    print("Check output.md!")