from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import main
import json

app = Flask(__name__)

headers = {
    'TRN-Api-Key':'cc0ff145-ca3a-4f12-82a0-7759c9927e52'
}

# TODO move to other file called Utilities
# build class
class baseInfo():
    def __init__(self, username, timeplayed, playerLevel, gearScore):
        self.username = username
        self.timeplayed = timeplayed
        self.playerLevel = playerLevel
        self.gearScore = gearScore

# use request library to return data
def getBaseInfo(username, headers):
    if username is not None:
        r = requests.get('https://public-api.tracker.gg/v2/division-2/standard/profile/uplay/'+username, headers=headers)
        data = json.loads(r.text)
        data = data['data']
        return data

def populateClass(className, dataVariable):
    objectName = className(
                username = dataVariable['platformInfo']['platformUserHandle'],
                timeplayed = dataVariable['segments'][0]['stats']['timePlayed']['displayValue'],
                playerLevel = dataVariable['segments'][0]['stats']['highestPlayerLevel']['value'],
                gearScore = dataVariable['segments'][0]['stats']['latestGearScore']['value']
            )
    return objectName

 

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def index1():
    if request.method == 'POST':
        
        username = request.form['username']     

        # check to see if username is empty
        if len(username) == 0:
            # handle for blank username
            print("user name is none")
            data = None
            message = "Please input a Username"
        else:
            # call function to retrieve API info and assign to baseInfoData variable
            baseInfoData = getBaseInfo(username, headers)
            # call function to fill class with baseInfoData, return data, and assign to variable called data
            data = populateClass(baseInfo, baseInfoData)
            message = None

    return render_template('index.html', data=data, message=message)
   




if __name__ == '__main__':
    app.debug = True
    app.run()