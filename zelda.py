
import os
import time
import sys
# import speech_recognition as sr
from twilio.rest import Client
from flask import Flask, request
from twilio import twiml
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from wit import Wit

# Perhaps something like this http://rasa-nlu.readthedocs.io/en/stable/index.html to handle offline intents 
# visual ai: https://www.clarifai.com/
# Existing OS ai https://github.com/Melissa-AI/Melissa-Core
#snowboy for hotword
# Could I get my AI to communicate with other AIs like ask a friend for help? If it is uncertain how to answer
# a query it could then ask Siri ect
# As one developer I can do little, Jarvis in iron man is what enables Stark to be so much more
# An Ai that can code will be vital

app = Flask(__name__)
WIT_AI_KEY = "PXIASINGVEDWFS3JOSJ3HKIU224GGLMF"  # Wit.ai keys are 32-character uppercase alphanumeric strings
w = Wit('PXIASINGVEDWFS3JOSJ3HKIU224GGLMF')

client = Client('AC69124796ce884c143582d3721d1c4321', '97ccece141f49dd41e65e11afda47820')

resp = w.converse('luffy',sys.argv[1],{})
e = resp['entities']

def get_value(e, entity):
	value = e[entity][0]['value']
	return value

for entity in e:
	print get_value(e, entity)


@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	message_body = message_body.lower()
	resp = w.converse('luffy',message_body,{})
	intent = resp['entities']['intent'][0]['value']
	# print resp['msg']
	# print resp['intent']
	# message = client.api.account.messages.create(to=number, from_="+61428073491", body=resp['msg'])
	# output(intent)
	# resp = twiml.Response()
	# resp.message('Hello {}, you said: {}'.format(number, message_body))
	intent = str(intent)	
	output(intent)	
	return 'works'

@app.route('/text', methods=['GET', 'POST'])
def text():
	 resp = w.converse('luffy',str(request.data),{})
	 print resp
	 intent = resp['entities']['intent'][0]['value']
	 intent = str(intent)
	 output(intent)
	 return 'returned'

def output(message_body):
	if 'pi' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAABoAAABbAw==')
	elif 'volume up' in message_body:
		i = 0
		while i < 10:
			os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAASAw==')
			i += 1
	elif message_body == 'tv volume down':
		i = 0
		while i < 10:
			os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAATAw==')
			i += 1
	elif 'mute' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAAUAw==')
	elif 'on' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAAVAw==')
	elif 'wake' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAAuAw==')
	elif 'off' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAAvAw==')
	elif 'sleep' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAAAvAw==')
	elif 'home' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAABgAw==')
	elif 'exit' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAQAAAAEAAABjAw==')
	elif 'component1' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAKQAAAA2Aw==')
	elif 'component2' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAKQAAAA3Aw==')
	elif 'stop' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAAYAw==')
	elif 'pause' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAAZAw==')
	elif 'play' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAAaAw==')
	elif 'subtitle' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAAoAw==')
	elif 'prev' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAA8Aw==')
	elif 'next' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAAJcAAAA9Aw==')
	elif 'hdmi1' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAABoAAABaAw=')
	elif 'hdmi3' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAABoAAABcAw==')		
	elif 'xbox' in message_body:
		os.system('./bravia-auth-and-remote/send_command.sh 192.168.1.5 AAAAAgAAABoAAABdAw==')

		





# def callback(recognizer, audio):
#     try:
#         said = r.recognize_wit(audio, key=WIT_AI_KEY)
#         print("Zelda thinks you said " + said)
#         print(r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)) 
#         os.system('curl -X POST -H "Content-Type: text/plain" --data ' + str(said) +  ' http://zelda.ngrok.io/text')
#     except sr.UnknownValueError:
#         print("Wit.ai could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from wit.ai service; {0}".format(e))


# r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# # start listening in the background (note that we don't have to do this inside a `with` statement)
# stop_listening = r.listen_in_background(m, callback)
# # `stop_listening` is now a function that, when called, stops background listening

# # do some other computation for 5 seconds, then stop listening and keep doing other computations
# for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening()  # calling this function requests that the background listener stop listening
# while True: time.sleep(0.1)

if __name__ == '__main__':
	app.run()


