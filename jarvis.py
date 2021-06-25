
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir")
    speak("Please tell me how may I help you") 


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"        
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail@gmail.com','your password')
    server.sendmail('yourgmail@gmail.com',to,content)
    server.close()


if __name__== "__main__":
    wishMe()


    while True:
    
        query= takeCommand().lower()



        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'F:\\songs\\abcd'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")  


        elif'hello friday' in query:
            speak("Hello sir, how are u?")    
        

      
        elif 'play old songs' in query:
             music_dir = 'F:\\songs\\old'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))

        elif 'how are you' in query:
            speak("I am fine sir, how about u ") 
            speak("Please take care  ,wash your hands regularly and wear mask")


        elif 'where do you live' in query:
            speak("You can find me on all kinds of devices, like phone and google homes")
            

        elif 'open atom' in query:
            codepath = "C:\ProgramData\ABHAY\atom\app-1.57.0"
            os.startfile(codepath)  


        elif 'email to abhay' in query:
         try:
                 speak("what should I say?")  
                 content = takeCommand()
                 to = "abhaygm07@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent")
         except Exception as e:
                 print(e)
                 speak("Sorry my friend Abhay. I am not able to send this email")

        elif 'quit' in query:
            exit()






      
