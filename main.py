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
    def __init__(self, username, timeplayed):
        self.username = username
        self.timeplayed = timeplayed
        
# initialize class and populate data
x = baseInfo(
    username = baseInfoData['platformInfo']['platformUserHandle'],
    timeplayed = baseInfoData['segments'][0]['stats']['timePlayed']['displayValue']
    )


# print(x.username, " ", x.timeplayed)