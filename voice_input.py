import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)      #reducing intencity of noise from input speech
        audio = r.listen(source)
        said = ""

        try:
            said  = r.recognize_google(audio)      #speech to text
            print(said)
        except Exception as e:
            print("Exception: "+str(e))

    return said

