from flask import Flask, render_template
import requests
import main

app = Flask(__name__)

headers = {
    'TRN-Api-Key':'cc0ff145-ca3a-4f12-82a0-7759c9927e52'
}

data = main.data.username

@app.route('/')
def index():
    return render_template('index.html', data=data)



















if __name__ == '__main__':
    app.debug = True
    app.run()