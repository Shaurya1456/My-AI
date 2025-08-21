# You Can Edit It And Make It Much More Better!
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
import pyautogui
import wolframalpha
import random
import psutil
import sys     
import pyjokes as pyj
import pyautogui as pya
import time
import wmi
from translate import Translator
import screen_brightness_control as sbc


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voice', voices[3].id)

def speak(audio):
    engine.say(audio)
    print(f"JARVIS: {audio}")
    engine.runAndWait()   

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

Time = datetime.datetime.now().strftime("%H:%M:%S")

usage = str(psutil.cpu_percent())
battery = psutil.sensors_battery()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
         speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
           speak("Good Afternoon Sir!")

    else:
         speak("Good Evening Sir!")

    speak(f"The Current Time Is {Time}. The Current Date Is {day, month, year}. The Computer Battery Is {battery.percent}%")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
         print("Recognizing...")   
         query = r.recognize_google(audio, language='en-us')
         print(f"Sir: {query}\n")

    except Exception as e:
        #print(e)

        print("Say That Again Please")
        return "None" 
    return query

def sendEmail(myemail,content):
    server = smtplib.SMTP("Your Email ID", 587)
    server.ehlo()
    server.starttls()
    server.login("Your Email ID", "Your password")
    server.sendmail("Your Email ID", to,content)
    server.close()

def cpu_battery_usage():
    cpu_usage = str(psutil.cpu_percent())
    speak(f"CPU Is At {usage}%")

    battery_usage = psutil.sensors_battery()
    speak(f"The Battery Is {battery.percent}%. {battery_usage}")

def jokes():
    speak(pyj.get_joke())


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Got It!")
            speak("According To Wikipedia-")
            print(results)
            speak(results)

        elif 'open youtube' in query:
             speak("Opening Youtube")
             webbrowser.open('https://www.youtube.com')   

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open('https://www.google.co.in')  

        elif 'open stack overflow' in query:
             speak("Opening Stackoverflow") 

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(strTime)
             speak(f"Sir The Time Is {strTime}")

        elif 'open sublime text' in query:
            Sublime_textPath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(Sublime_textPath)

        elif 'who are you' in query:
             speak("I am Jarvis. Your Personal Assistant") 

        elif 'search google' in query:
            speak("Sir, What Should I Search On Google?")
            Google = query.replace("google", "")
            Google_Search = takeCommand()
            speak(f"Searching For {Google_Search} In Google") 
            webbrowser.open(f"https://www.google.com/search?q={Google_Search}")

        elif 'search youtube' in query:
            speak("Sir, What Should I Search On Youtube?") 
            Youtube = query.replace("youtube", "")
            Youtube_Search = takeCommand()
            speak(f"Searching For {Youtube_Search} in Youtube")
            speak("Here We Go To Youtube")
            webbrowser.open(f"https://www.youtube.com")   

        elif 'who made you' in query:
            speak("Sir, I Was Made By Tony Stark In The MCU. But You Made Me!")

        elif 'jarvis you there' in query:
            speak("At Your Service Sir!")  

        elif 'how are you' in query:
            speak("I am Fine Sir!")

        elif 'search amazon' in query:
            speak("What Should I Search On Amazon?")
            Amazon = query.replace("amazon", "")
            Amazon_Search = takeCommand()
            speak(f"Searching {Amazon_Search} In Amazon")
            webbrowser.open(f"https://www.amazon.in/s?k={Amazon_Search}")   

        elif 'jarvis you up' in query:
            speak("For You Sir, Always!")   

        elif 'hello' in query or 'hello jarvis' in query:
            speak("Hello Sir!")

        elif 'jarvis you there' in query:
            speak("At Your Service Sir!")  

        elif 'open skype' in query or 'open sky' in query:
            speak("Opening Skype!") 
            wb.open_new_tab("https://www.web.skype.com")

        elif 'battery' in query:
            cpu_battery_usage() 

        elif 'by' in query or 'goodbye' in query or 'good bye' in query or 'terminate' in query:
            speak("Bye Sir!. Have A Good Day!")
            sys.exit()

        elif 'repeat' in query:
            speak("Alright!")
            repeat = takeCommand()
            speak(repeat) 

        elif 'joke' in query:
            jokes()  

        elif 'write a note' in query:
            speak("What Should I Note?")   
            notes = takeCommand()
            file = open('notes.txt', 'w')  
            speak("Sir, Should I Include Date And Time")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Date_Time_Ans = takeCommand()
            if 'yes' in query or 'sure' in Date_Time_Ans:
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Sir, I Have Taken A Note Of That")
            else:
                 file.write(notes)
        
        elif 'show notes' in query:
            speak("Showing Notes")
            file = open('notes.txt', 'r')
            speak(file.read())

        elif 'remember this' in query:
            speak("What Should I Remember?")
            memory = takeCommand()
            speak(f"You Asked Me To Remember {memory}")
            remember = open("memory.txt", 'w') 
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open("memory.txt", 'r') 
            speak(f"You Asked Me To Remember {remember.read()}")

        elif 'where is' in query:
            location = query.replace('where is', '')  
            where_loaction = location
            speak(f"Locating {where_loaction}") 
            wb.open_new_tab(f"https://www.google.co.in/maps/place/{where_loaction}")

        elif 'stop listening' in query:
            speak("For How Many Minutes Should I Stop Listening?") 
            ans = int(takeCommand()) 
            time.sleep(ans)

        elif 'log off' in query:
            speak("Your PC Is Going To Shut Down In 20 Sec. Make Sure You Exit From All Applications")
            time.sleep(20) 
            os.system('shutdown -l')   

        elif 'restart' in query:
            speak("Reastarting Your Device")
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            speak("Your PC Is Going To Shut Down In 20 Seconds. Make Sure You Exit From All Applications")
            os.system("shutdown /s /t 1")

        elif 'save' in query:
            speak("Saving This")
            pya.hotkey('ctrl', 's')

        elif 'copy this' in query:
            speak("Copying To Clipboard")  
            pya.hotkey('ctrl', 'c') 

        elif 'paste this' in query:
            speak("Pasting This") 
            pya.hotkey('ctrl', 'v')  

        elif 'open new tab' in query:
            speak("Opening New Tab")
            pya.hotkey('ctrl', 'n')

        elif 'undo' in query:
            speak("Undoing This")
            pya.hotkey('ctrl', 'z')

        elif 'redo' in query:
            speak("Redoing This")
            pya.hotkey('ctrl','y')

        elif 'open notepad' in query:
            speak("Opening Notepad")
            notepad_Path = 'notepad.exe' 
            os.startfile(notepad_Path)

        elif 'page up' in query:
            speak("Going Up")
            pya.hotkey('pageup') 

        elif 'page down' in query:
            speak("Going Down")
            pya.hotkey('pagedown')

        elif 'open new tab' in query:
            speak("Opening New Tab")
            pya.hotkey('ctrl', 't')
    
        elif 'refresh' in query:
            speak("Refreshing")
            pya.hotkey('F5')

        elif 'play music' in query:
            music()    

        # elif 'take a screenshot' in query:
        #     speak("Sir, By What Name Should I Save It?")   
        #     screenshot_name = takeCommand()
        #     speak("Ok Sir, Taking A Screenshot.")
        #     pya.screenshot("C")

        elif 'open command prompt' in query:
            speak("Opening Command Prompt")
            os.system("start cmd")

        elif 'open windows explorer' in query:
            speak("Opening Windows Explorer")
            os.system("explorer")

        elif 'new folder' in query:
            speak("Making New Folder")
            pya.hotkey('ctrl', 'shift', 'n')

        elif 'open microsoft edge' in query:
            speak("Opening Micrososft Edge")
            pya.hotkey('ctrl', 'alt', 'M')

        elif 'inspect' in query:
            speak("Inspecting")
            pya.hotkey('F12')

        elif 'full screen' in query:
            speak("Entering Full Screen Mode")
            pya.hotkey('f')

        elif 'change monitor brightness' in query:
            speak("To What Brightness Sir?")
            Brightness = takeCommand()
            speak("Ok Sir")
            monitors = sbc.list_monitors()
            # print(monitors)
            # now use this to adjust specific screens by name
            sbc.set_brightness(Brightness, display=monitors[0])

        elif 'translate to' in query:
            lang = query.replace('translate to', '')
            translator = Translator(to_lang=lang) 
            speak("Sir, What Should I Translate?")
            while True:
                line = takeCommand()
                if 'stop' in line:
                  speak("Ok Sir") 
                  time.sleep(2)

                translation = translator.translate(line)
                print(f"Translated To {lang}")
                speak(translation)

        elif 'set an alarm' in query:
            hour = int(input("Enter The Hour: "))
            minn = int(input("Enter The Minutes: "))
            sec = int(input("Enter The Seconds: ")) 
            n = 5 
            print(f"Alarm Set For {str(hour)} {str(minn)} {str(sec)}") 
            speak(f"Alarm Set For {str(hour)} {str(minn)} {str(sec)}")
            while True:
                if time.localtime().tm_hour == hour and time.localtime().tm_min == minn and time.localtime().tm_sec == sec:
                 print("Wake Up Sir!!!")
                 playsound("Alarm File Location")  

        elif 'show me' in query:
            pic = query.replace('show me', '')
            pictures = f'https://www.google.co.in/search?q={pic}'
            speak("Sure Sir!")
            speak(f"Searching Pictures Of {pic}") 
            wb.open_new_tab(pictures)

