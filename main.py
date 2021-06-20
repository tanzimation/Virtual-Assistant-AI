import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
tanzim = pyttsx3.init()
voices = tanzim.getProperty('voices')
tanzim.setProperty('voice', voices[0].id)


def talk(text):
    tanzim.say(text)
    tanzim.runAndWait()


def take_command():
    try:
        with sr.Microphone() as push:
            print('listening...')
            voice = listener.listen(push)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tanzim' in command:
                print(command)
                command = command.replace('tanzim', '')
            else:
                print("Sorry")

    except:
        pass
    return command


def run_tanzim():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %S')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hate' in command:
        talk('I love you')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_tanzim()
