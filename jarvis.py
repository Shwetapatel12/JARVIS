import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit 
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


#Intialize the pyttsx3 engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[len(voices) - 1].id)

# text to speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# speech recognition function to convert voice to text
def TakeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source,timeout=5,phrase_time_limit=10)

    try:
        print("Recognizing....")
        query = recognizer.recognize_google(audio, language="en_in")
        print(f"user said: {query}")
        speak({query})
    
    except sr.WaitTimeoutError:
        print("Listening timed out, please try again ")
        return None
    
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query
    
# to wish
def Wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour<=12:
        speak("GOOD MORNING")

    elif hour >= 12 and hour<=16:
        speak("GOOD AFTERNOON")
    
    elif hour >= 16 and hour<=21:
        speak("GOOD EVENING")
    
    else: 
        speak("GOOD NIGHT")
    speak("I am jarvis sir. please tell me how can i help you")
 
# to send email
# def sendEmail(to,content):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com',587)
#         server.ehlo()
#         server.starttls()
#         server.login('shwetapatel0712@gmail.com', '0712jbp@123')
#         server.sendmail('shweta0712@gmail.com', to, content)
#         server.close()
#         # speak("email  has been se/nt")
    
    # except Exception as e:
    #     print(e)
    #     speak("sorry , I am not able to send this email")
        
# def news():
#     main_url = 


if __name__ == "__main__":
    # speak("Hello, how can i help you?")
    # command = TakeCommand().lower()
    # if 'hello' in command:
    #     speak("Hello!, How are you? ")
    # TakeCommand()
    Wish()
    while True:
    # if 1:

        query = TakeCommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath ="D:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may i help you? ')

        
        elif "open adobe reader" in query:
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader XI.lnk"
            os.startfile(apath)


        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open vs code" in query:
            os.system("code")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir ="D:\\Song"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            # os.startfile(os.path.join(music_dir, rd))
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        
        elif "wikipedia" in query:
            speak("searching wikipedia.......... ")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=5)
            speak("according to wikipedia")
            speak(result)
            # print(result)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open Facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")

        # elif "open WhatsApp" in query:
        #     webbrowser.open("www.whatsapp.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = TakeCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+919302824557","how are you",22,46)
            time.sleep(120)
            speak("message has been sent")


        elif "play song on youtube" in query:
            kit.playonyt("see you again")
              
        elif 'timer' in query or 'stopwatch' in query:
            speak("for how many minutes? ")
            timing = TakeCommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('your time has been finished sir')
        # elif "email to shweta" in query:
            # try:
            #     speak("what should i say? ")
            #     content = TakeCommand().lower()
            #     to ="9303shraddha@gmail.com"
            #     sendEmail(to,content)
            #     speak("Email has been sent to shweta")

            # except Exception as e:
            #     print(e)
            #     speak("sorry sir , i am not able to sent this mail to shweta")
        
        # to close any application
        

        
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()


# to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

#to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "D:\\Song"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        

# to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut dowm the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerof.dll,setSuspendState 0,1,0")


        speak("sir , do you have any other work")



            
                

        


        

        

    