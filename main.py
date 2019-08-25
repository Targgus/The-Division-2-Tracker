import requests
import json



# header data
headers = {
    'TRN-Api-Key':'cc0ff145-ca3a-4f12-82a0-7759c9927e52'
}

# variable for username
username='Targgus'

# use request library to return data
def getBaseInfo(username, headers):
    r = requests.get('https://public-api.tracker.gg/v2/division-2/standard/profile/uplay/'+username, headers=headers)
    data = json.loads(r.text)
    return data['data']

# call function
baseInfoData = getBaseInfo(username, headers)

# print(baseInfoData['segments'][0]['stats']['timePlayed']['displayValue'])

# build class
class baseInfo():
    def __init__(self, username, timeplayed, playerLevel, gearScore):
        self.username = username
        self.timeplayed = timeplayed
        self.playerLevel = playerLevel
        self.gearScore = gearScore
        
# initialize class and populate data
data = baseInfo(
    username = baseInfoData['platformInfo']['platformUserHandle'],
    timeplayed = baseInfoData['segments'][0]['stats']['timePlayed']['displayValue'],
    playerLevel = baseInfoData['segments'][0]['stats']['highestPlayerLevel']['value'],
    gearScore = baseInfoData['segments'][0]['stats']['latestGearScore']['value']
    )


# print(x.username, " ", x.timeplayed)