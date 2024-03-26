# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import subprocess

engine = pyttsx3.init('nsss')  # driver for voice in getting the voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # here u choose the tone 0 for male and 1 for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wisheme():
 
    hour = int(datetime.datetime.now().hour);
    minutes = int(datetime.datetime.now().minute);
    
    if hour >= 12:
     speak("Good evening Sir")
    elif hour<12:
     speak("Good morning sir")


    speak("Welcome back sir. I am ready for tasking");
    speak("the time is ");
    speak(str(hour));
    speak(str(minutes));
    speak("Let me know how to help you. What are you looking for");


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening");
        r.pause_threshold = 1;
        audio = r.listen(source)

    try:
        print("recongizing your command")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said:{query}\n");
    except Exception as e:
        print("say again bitte....")
        return "None"

    return query




if __name__ == '__main__':
    wisheme()


    while True:
        query = take_command().lower()

        if 'open wikipedia' in query:
            speak("what do u want from wikipedia sir")
            query = take_command().lower()
            query = query.replace("wikipedi", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        #opening some computer applications

        if 'open notepad ' in query:
            subprocess.call(["/bin/bash", "-c", "open /System/Applications/Notes.app"])


        if 'open calculator' in query:
            subprocess.call(["/bin/bash", "-c", "open /System/Applications/Calculator.app"])

        #opening some browsers
        if 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        if 'open chrome' in query:
            webbrowser.open('https://www.chrome.com/')

        if 'open bing' in query:
            webbrowser.open('https://www.bing.com')

        if 'go offline' in query:
            speak(" going offline ")
            break

        
        






