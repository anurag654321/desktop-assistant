import speech_recognition as sr
import pyttsx3
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()
    
def start():
    print("hello i am desktop assistant.")
    say("hello i am desktop assistant")
    print("how can i help you")
    say("how can i help you.")
    
def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        say("i am waiting say something")
        listen()
    except sr.RequestError as e:
        say(f"try again {e}")
        listen()
    return text




if __name__ == "__main__":
    # start()
   
    while True:
        voice=listen()
        if "hello" in voice.lower():
            say("hello how can i help you")
        if "exit" in voice.lower():
            say("have a good day")
            exit()
        if "open chrome" in voice.lower():
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google chrome')
        if "open youtube" in voice.lower():
            webbrowser.open_new_tab("https://www.youtube.com")
        if "open code" in voice.lower():
            os.startfile('C:/Users/anrag/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code')
        if "open google" in voice.lower():
            webbrowser.open_new_tab("https://www.google.com")
        
        
        