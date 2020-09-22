# You can edit and make it much more better!
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import smtplib
import sys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    print(f"SAM: {audio}")
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"Sir Said: {query}")

    except Exception as e:
        print("Please Say That Again...")
        return "None"
    return query

speak("Sam At Your Service Sir!")


if __name__ == '__main__':
    while True:

        query = takeCommand().lower()

        if 'open notepad' in query:
            notepad_path = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(notepad_path)

        elif 'open command prompt' in query:
            speak("Ok Sir, Opening Command Prompt")
            os.system('start cmd')

        elif 'open powershell' in query:
            speak("Ok Sir, Opening Powershell")
            os.system('start powershell')

        elif 'play music' in query:
            music_dir = 'C:\\music(songs)\\noncritical\\favoruitesongs2'
            songs = os.listdir(music_dir)
            random_songs = random.choice(songs)
            speak("Here's Your Music. Enjoy!")
            os.startfile(os.path.join(music_dir, random_songs))


        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia-")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query:
            speak("Ok Sir, Opening Youtube")
            webbrowser.open('https://www.youtube.com')


        elif 'open facebook' in query:
            speak("Ok Sir, Opening facebook")
            webbrowser.open('https://www.facebook.com')

        elif 'open stack overflow' in query:
            speak("Ok Sir, Opening Stackoverflow")
            webbrowser.open('https://www.stackoverflow.com')

        elif 'goodbye sam' in query:
            speak("Good Bye Sir, Have a Good Day!")
            sys.exit()
            
        elif 'movie review' in query:
            speak("Sir, What Is The Name Of The Movie?")
            movie = query.replace('search', '')
            movie_name = takeCommand()
            speak(f"Ok Sir, Searching {movie_name} movie review")
            webbrowser.open(f'https://www.google.co.in/search?q={movie_name} movie review')
            
        elif 'play videos' in query:
            video_dir = 'E:\\Videos'
            videos = os.listdir(video_dir)
            random_videos = random.choice(videos)
            speak("Here's Your Videos, Enjoy!")
            os.startfile(os.path.join(video_dir, random_videos))
            
        elif 'open chrome' in query:
            GC_Path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            speak("Ok Sir, Opening Google Chrome")
            os.startfile(GC_Path)

        elif 'open code' in query:
           VSCode_Path = "C:\\Users\\Sony\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           speak("Ok Sir, Opening Visual Studio Code")
           os.startfile(VSCode_Path)
           
        elif 'search google' in query:
            speak("Ok, What Can I Search For You In Google?")
            Google = query.replace('search', '')
            Google_search = takeCommand()
            speak(f"Ok Sir, Searching {Google_search}")
            webbrowser.open(f'https://www.google.co.in/search?q={Google_search}')

            
