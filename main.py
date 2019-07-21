import sys
sys.path.insert(0, 'lib')

import requests
import json
import sys
from flask import Flask
from flask import render_template
from flask import request

sys.path.insert(0, 'lib')


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/form/')
@app.route('/form/<name>')
def form(name=None):
    return render_template('form.html', name=name)

@app.route('/send/', methods=['POST'])
def send():
    name = request.form['name']
    message = request.form['message']
    if name and message != "":
        message_type = {
    		  "text": "Message",
    		  "username" : "Un message de "
              }
        message_type['text'] = message
        message_type['username'] = name
        jsondata = json.dumps(message_type)
        r = requests.post('slack_webhook_url', data = jsondata)
        #print(r.status_code)
        return render_template('merci.html', name=name)
    else:
        return render_template('send_error.html', name=name)


if __name__ == "__main__":
    app.run()
