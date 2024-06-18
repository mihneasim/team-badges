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

## Sample Output

### All Badges

|  Badge | Description |  Badge | Description |
|---|----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Clean Power](badges-img/broom.png "Simplified and cleaned-up older code")  | **Clean Power** <br> Simplified and cleaned-up older code. Awarded for people going the extra mile in not just delivering their user story, but also cleaning up any related code! | ![Release Saviour](badges-img/super-hero.png "Simplified and cleaned-up older code") | **Release Saviour** Jumped in and addressed a bug holding up a roll-out. This is awarded every time somebody stood out while investigating a nasty blocker during the deployment process.  |
| ![SCA Ruler](badges-img/sca.png "Addressed a vulnerability as reported by SCA.")  | **SCA Ruler** <br> Jumped in and upgraded a vulnerable library as reported by Software Composition Analysis process. |  | |

### Awarded Badges

#### Amy Santiago

<img src="badges-img/broom.png" title="Earned 2024-06-11: Removed all the legacy of user session logic in old stack modules." width="80">
<img src="badges-img/super-hero.png" title="Earned 2024-03-04: Saved the day when figuring out the traffic spikes on Offers Service when releasing the new checkout page." width="80">

#### Ray Holt

<img src="badges-img/broom.png" title="Earned 2024-06-11: Removed deprecated methods in application state manager" width="80">
<img src="badges-img/sca.png" title="Earned 2024-06-18: Found that old project still using the vulnerable 2.15.0 Log4J" width="80">

