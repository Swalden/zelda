
import time
import os
import speech_recognition as sr

# this is called from the background thread
# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     try:
#         said = r.recognize_google(audio, key="a024e8MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCsfsgANMPvFJyrsJxur6l++hOqmz5befakl7xrFoqAFuqm1wxeE6FJl4sxeTTTir5NbDpdjl9AzOaw2/UYH03pcrIvYgkS2XT8fb1HRj4v9yxGMGKylfrGF6/6GPFeXC2/Bm0WohBCrUM3Cm4DP/grlfl+bt946/7OXDvgZcypPT4tY6jWMCPTMEdqu2op/0z86SNTznW4X5cM9Q3FO6EDheryuVqhykTXFbOEfjE/tfR3LDMUuGcrwPFdOXnrrrpe2xV9RYkg4PdCqQ50sCCrzS2CVnw6BUKt27SvNw2A28+DgCoxzXLZusAsWMEV4HhLfZ/nPhk7J36joE351JqtAgMBAAECggEAd3e/cVUaNuXhtI+3aHnFPKpbIJgw0g5gopJs7wZHmntEvZTHfgi+dke9IeC+k5zOPLUun0lR84F2bRuKXtCfl4XWnzaY7jMp8Q3tIAYoX/Qi9+HfGa0CaFxThzXrRd012c3LlBdeh6+Uk/RnSVzuttFCYSzNHeTlL2t2FO6slrEupIJSn7tvdB5IyZB68hijSyDE2Sa0sSXW/l3HRahNzw2loG786AMP0splPWh5AD1nESHDKeM85UC0QIYSLYcTLMtMcYW0xeTaffD9oVSAiS7neVTx2SegKJPoviDn10DPRV3XFTCpoZfyn/yavsrc1sWUVPaK9w7hudBvjiS0CQKBgQDarJN5KnaipL+zUk+Phnk1ZOMIWpbdOvo2hJxTj19YlgIwGefRjFSWtfLB2DFua1p4BQddeCb472N4QWA3RUwJWzKXM96U/n5EBwWdIGhFxOdw6HIigykCwdeZ3QhJUgPFGvtvkmKvnlL1tn1w50Cc/w6xZ9E9Mm1ExbD+/GLZvwKBgQDJ8FJxBABwHgR8/qlwqOU7NMgqu22A9eW+LZsUF77HBAnHG52ECTiWqvc+vT56bitelavX4X99r8jWzhI1jl0Am1lkDlm1kPoZLWIoB6S8Si0Oe0DLeQPVzGLwkNyxb0hxbXyX9BMz1spAvjYIxZCHd7CZAOGNO/CI75kwbd7ukwKBgFQvB/8nd9CZeCuCzppEfLkvg6+doGK+58DBQKVylpQ1+9Wkw3gKfC4hEbnKjw0hSwzVcsZrESXYkwSitnXQubsIXuuSzmexqc5qnaCl7z6c1TTEZ9wdflZPZb8YNq5zYnwpLQ8A3fkaDHoHrTcf7+IA1xk5DHZwyVwmd0NSyoNlAoGAK7Ih1Kyd/6SvKfDc7zDMsVwBeCWoU0BiHx21McrVkDDSgM/77IcmRIvoBh5i95EBN21BiuwTbznrRne+vvH4M9pppFnqlXwyceI9HBZTUh7m0vxej+i2qLuaKR3fc1F2Jn0fea3pvczbZNkDzjAZzwZaIzFqnOn8aVUXG8CafZsCgYEAsMUKURcSjmfDFt9nZOQTrk5AeXzGwdLct6dFjRfMpvfVboBrjGA66wMWiJMczk6EU+p7EUf3k0TA6BOfE5fJeTAH5CWdavp1icZFfGDeLOZsncqBeHo2ngJxQvKiTFHFxBPbVkJwcZcGD0yEOjhhWm4bHKwz1YhwRPsCGifgOAM=1c1db10ab5c064664840503fb39ba5229e")
#         print("Google Speech Recognition thinks you said " + said)
#         os.system('curl -X POST -H "Content-Type: text/plain" --data ' + str(said) +  ' http://zelda.ngrok.io/text')
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
def callback(recognizer, audio):
    WIT_AI_KEY = "PXIASINGVEDWFS3JOSJ3HKIU224GGLMF"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        said = r.recognize_wit(audio, key=WIT_AI_KEY)
        print("Zelda thinks you said " + said)
        print(r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)) 
        os.system('curl -X POST -H "Content-Type: text/plain" --data ' + str(said) +  ' http://zelda.ngrok.io/text')
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from wit.ai service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone(device_index=2)
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
stop_listening()  # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)
