import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail
#from playsound import playsound # required to play music

engine = pyttsx3.init(
    'sapi5')  # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')  # gets you the details of the current voices
engine.setProperty('voice', voices[1].id)  # 1-male voice , 0-female voice


def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us


def wishme():  # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning')

    elif 12 < hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello , I am Bubble Boy, your Voice assistant. Please tell me how may I help you')


def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:  # error handling
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')  # 'say that again' will be printed in case of improper voice
        return 'None'
    return query


def sendemail(to, content):  # function to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email.com', 'login_password')
    server.sendmail('email_address@gmail.com', to, content)
    server.close()


if __name__ == '__main__':  # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            speak('okay boss')
            music_dir = r'FILE_PATH'
            songs = os.listdir(music_dir)
            playsound(os.path.join(music_dir, songs[1]))
            #os.startfile(os.path.join(music_dir, songs[0]))


        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')


        elif 'who created you' in query or 'who made you' in query :
            speak('I was created by my boss VGNESHWARI S')


        elif 'open gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'open amazon' in query:
            webbrowser.open('amazon.in')

        elif 'pycharm' in query:
            codepath = 'pycharm_directory_of_your_computer'
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak('what should i write in the email?')
                content = takecommand()
                to = 'reciever_email@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me. Bye Bye')
            quit()
