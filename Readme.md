Gamification is one way to bring more recognition to team members performing contributions that stand out.

This simple repo offers a light framework for versioning badges and awards to team members, in simple .yml files.
Running the python script, it will write a .md overview of all the data.

## Instructions


1. Setup virtual env: `python -m venv .`
1. Activate virtual env: `. bin/activate`
1. Install deps: `pip install -r requirements.txt`
1. Continuously update `badges.yml` with awards tailored to your team and your organizational context.
1. Every time someone earns an award, grant the badge in `team.yml`. Add a date and, optionally, a specific description for the relation Team Member <-> Badge.
1. Regenerate markdown and use it in your platform of choice for presentation layer: `python main.py # output in badges.md and team.md`