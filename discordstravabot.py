#!/usr/bin/env python3
''' Strava Integration for Discord
Made for Discord Hack Week 2019 '''
import os
import sys
import discord

# Grab the Discord bot token from DISCORDTOKEN environment variable
DISCORDTOKEN = os.environ.get('DISCORDTOKEN')
if DISCORDTOKEN is None:
    print("DISCORDTOKEN variable not set. Unable to launch bot.")
    sys.exit()
else:
    print("Discord token is", DISCORDTOKEN)

# Grab the Strava auth token from STRAVATOKEN environment variable
# This is used for Bearer authentication against Strava's API
STRAVATOKEN = os.environ.get('STRAVATOKEN')
if STRAVATOKEN is None:
    print("STRAVATOKEN variable not set. Unable to launch bot.")
    sys.exit()
else:
    print("Strava token is", STRAVATOKEN)

class StravaIntegration(discord.Client):
    async def on_ready(self):
        ''' Function fires when bot connects '''
        print('Logged on as', self.user)

    async def on_message(self, message):
        ''' Primary inbound message parsing function '''
        print('Message:', message.content)
        if message.author == self.user:
            return

        if message.content == '!leaderboard':
            await message.channel.send('Showing leaderboard.')

client = StravaIntegration()
client.run(DISCORDTOKEN)
