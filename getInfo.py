import codes
import requests


def getGameIDsForLeague(LEAGUE_ID):
    matchIDToSkipTo = ""
    IDList = []
    while(True):
        url = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={codes.API_Key}&league_id={LEAGUE_ID}' + \
            "&start_at_match_id=" + str(matchIDToSkipTo)
        r = requests.get(url)
        print(f'REQUESTING: \n' + url)
        request = r.json()
        for match in request['result']['matches']:
            matchID = int(match['match_id'])
            if matchID in IDList:
                continue
            IDList.append(matchID)
        if int(request["result"]["results_remaining"]) != 0:
            matchIDToSkipTo = request['result']['matches'][-1]['match_id']
        else:
            return IDList
