import pyttsx3
import speech_recognition as sr
import random
import datetime
import pyjokes
import wikipedia

engine=pyttsx3.init('sapi5') #Sapi5 - text to speech engine developed by MS.
voice=engine.getProperty('voices') #So Envinor can talk.
speech_rate=engine.getProperty('rate') #To control the speed at which Envinor talks.
engine.setProperty('voices',voice[1].id)#Female version
#engine.setProperty('voices',voice[0].id) Male version
engine.setProperty('rate',135) #Lower the rate slower Envinor talks.

#Text to speech function, so Envinor can talk to us
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Speech to text, so Envinor can listen to what we are saying.
def listening():
    hear=sr.Recognizer()
    while True:
        with sr.Microphone() as source: 
            print('Envinor is listening....')
            audio=hear.listen(source)
            try:
                query=hear.recognize_google(audio) #Try to search on Google
                speak(query)
                print(query)
                return(query)
            except:
                speak('I didnt quite catch that, could you repeat it again?')
                print("I didn't quite catch that, could you repeat it again?")

while True:
    query=listening().lower()

    #Response for different cases
    if 'name' in query:
        choices=['Hey','Hi','Hello']
        speak(f'{random.choice(choices)}, my name is Envinor. I am your friendly virtual assistant!')
    
    elif 'how are you' in query:
        choices=['I am splendid!','I am good!','Pretty good!']
        speak(f'{random.choice(choices)}, how about you?')
    
    elif 'time' in query:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"It's currently {time}")
    
    elif 'date' in query:
        date=datetime.datetime.now().strftime('%d%m%y')
        speak(f"Today's date is {date}")

    elif 'search on wikipedia' in query:
        query=query.replace('search on wikipedia','')
        speak(wikipedia.summary(query,2))

    elif 'jokes' in query:
        speak(pyjokes.get_joke())

    elif 'bye' in query:
        choices=['Bye!','See you later!','Toodles','Have a nice day!']
        speak(random.choice(choices))
        break

    else:
        speak("I didn't understand, what you were trying to tell.")