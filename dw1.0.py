import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import sys
import datetime

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    print(words)
    engine.runAndWait()

talk("Привет,я Wela! Спроси у меня что хочешь!")

record = sr.Recognizer()
microphone = sr.Microphone()
url = "http://www.google.ru/"
url_1 = "https://www.youtube.com/"
url_2 = "https://vk.com/audios548992932"
vremya = datetime.datetime.now()

def ProgrammRun(text):
    if str(text) == "открыть браузер":
        webbrowser.open(url)
        talk("Открываю")
    elif str(text) == "стоп":
        talk("До свидания!")
        sys.exit()
    elif str(text) == "открой youtube":
        webbrowser.open(url_1)
        talk("Открываю YouTube")

def time(text):
    if str(text) == "скажи время":
        talk("Сейчас " + str(vremya.hour) + ":" + str(vremya.minute))
def anekdot(text):
    if str(text) == "расскажи анекдот":
        talk("Я бот,и не знаю анекдоты,поэтому...")
def dop(text):
    if str(text) == "кто твой создатель":
        talk("Я незнаю! Я бот!")
    if str(text) == "включи музыку":
        talk("Ла-Ла-Ла,открываю!")
        webbrowser.open(url_2)

try:
    while True:
        with microphone as source:
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source)
            result = record.recognize_google(audio,language="ru_RU")
            result = result.lower()
            print(format(result))
            ProgrammRun(format(result))
            time(format(result))
            anekdot(format(result))
            dop(format(result))

except sr.UnknownValueError:
    print("Ошибка,попробуйте снова!")

