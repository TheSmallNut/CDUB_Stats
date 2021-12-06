import codes
import requests
import json
import getInfo
LEAGUE_ID = 13721


CDUB_Games = getInfo.getGameIDsForLeague(LEAGUE_ID)

for game in CDUB_Games:
    print(game)
