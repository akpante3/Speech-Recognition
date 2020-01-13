import speech_recognition as sr
import webbrowser
import time
# from time import ctime

# initialize the recognizer
r = sr.Recognizer() 

# use the microphone
def record_audio(ask = False):
    if ask:
        print(ask)
    
    with sr.Microphone() as  source:
        print('Say something')
        audio = r.listen(source)
        voice_data=''
        try:
            # whatever is said it will be saved in this variable
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    print(voice_data == 'what is your name')
    if 'what is your name' in voice_data:
        print('My name is Robocob')
    if 'what is the time' in voice_data:
        print(time.ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want yo search for?')
        url = 'https:/google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what location')
        url = 'https:/google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is your location ' + location)
    if 'exit' in voice_data:
        exit()



time.sleep(1)
print('How can i help you')
while 1:
    voice_data =record_audio()
    print(voice_data )
    respond(voice_data)
