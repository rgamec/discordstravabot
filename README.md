# Discord Strava Bot
A Discord Strava Bot. Being made for the Discord Community Hack Week (2019). Work in progress.

## Installation and Usage
Sign up for Strava API access, then fill in the `DISCORDTOKEN`, `STRAVATOKEN`, and `STRAVACLUB` environment variables in the botlauncher.sh file. Then execute botlauncher.sh.

### Commands Supported
Currently `!leaderboard` (per week) and `!statistics` are implemented.

![DiscordStravaBot Screenshot](https://raw.githubusercontent.com/rgamec/discordstravabot/master/screenshot.png)

## Todo
* Authenticate against the Discord API [DONE]
* Authenticate against the Strava API [DONE]
* Add a `!leaderboard` command to show the top five users (by distance, for the current week) [DONE]
* Add a `!statistics` command to show the total distance covered by the group [DONE]
* Add a launcher script [DONE]
* Near real-time updates whenever a new activity is uploaded to the Strava group [WORK IN PROGRESS]
