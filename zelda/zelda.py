import os
from twilio.rest import Client
from flask import Flask, request
from twilio import twiml
import braviacodes

print braviacodes
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	print message_body
	if message_body == 'pi':
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.3 AAAAAgAAABoAAABbAw==')
	resp = twiml.Response()
	resp.message('Hello {}, you said: {}'.format(number, message_body))
	return str(resp)

if __name__ == '__main__':
	app.run()

client = Client('AC69124796ce884c143582d3721d1c4321', '97ccece141f49dd41e65e11afda47820')

