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

    team_tpl = env.get_template("team-member.md")
    badge_tpl = env.get_template("badge.md")
    try:
        os.unlink('badges.md')
    except FileNotFoundError:
        pass
    try:
        os.unlink('team.md')
    except FileNotFoundError:
        pass

    with open('badges.md', 'a') as output_file:
        badge_tuples = []
        previous = None
        for (index, badge) in enumerate(badges.values()):
            if (index % 2 == 1):
                badge_tuples.append((previous, badge))
                previous = None
            else:
                previous = badge
        if previous is not None:
            badge_tuples.append((previous, None))

        output_file.write(badge_tpl.render(badge_tuples=badge_tuples))

    with open('team.md', 'a') as output_file:
        for user in team:
            output_file.write(team_tpl.render(badges=badges, user=user))
    print("Check badges.md and team.md!")