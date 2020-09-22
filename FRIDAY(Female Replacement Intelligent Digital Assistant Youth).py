import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening!")

    speak("Hello Boss, I am Friday. How Can I Assist You")
def takeCommand():



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='EN-US')
        print(f"Boss Said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say tht again")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic of executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia... Please Wait...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=8)
            speak("According To wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Ok, opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Ok, Opening Google")
            webbrowser.open("https://www.google.co.in")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"The time is{strTime}")

        elif 'open stack overflow' in query:
            speak("Ok, Opening Stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
            
        elif 'who are you' in query:
            who_are_you_msg = ['I am Friday', 'My name Friday']
            speak(random.choice(who_are_you_msg))

        elif 'play music' in query or 'hit some music' in query:
            music_msg = ['Ok, Hitting Some Music', 'Ok']
            music_dir = 'music(songs)\\noncritical\\favroitesongs2'
            
        elif 'repeat me' in query:
            speak("Alright!")
            repeat = takeCommand()
            speak(repeat)





            
            
            
            

            
                



