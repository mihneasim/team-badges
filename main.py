import yaml
from pprint import pprint

try:
    with open('badges.yml', 'r') as yaml_file:
        badges = yaml.safe_load(yaml_file)
    with open('team.yml', 'r') as yaml_file:
        team = yaml.safe_load(yaml_file)
except:
    exit("Error reading yml files")

# pprint(badges)
# pprint(team)


for (member, props) in team.items():
    print(props, "\n")