#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import os

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    start = "Say Hey"
    print(start)
    os.system(start)
    audio = r.listen(source)

def hear():
        # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


ask_help = "what can i do for you?"

k = r.recognize_google(audio)

if "pradeep" in k.lower():
    print(ask_help)
    os.system("Say"+ " "+ "Hi, Pradeep")

elif r.recognize_google(audio) == "hello":
    print(ask_help)
    os.system("Say" + " " + ask_help)

elif r.recognize_google(audio) == "how are you":
    os.system("Say" + " " + "I am great, how are you")

else:
    print("I didn't hear you")
    os.system("Say" + " " + "I didnt hear you")
    hear()

#some regular expression

def re():
    someTxtis = "give test"
    os.system("Say" + " " + "a try block for the test case")
