import speech_recognition as sr
import pyttsx3

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue connecting to the service.")
        return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is your name" in command:
        speak("I am your virtual assistant.")
    elif "who made you" in command:
        speak("Sir Aditya created me. He was God for me. ")
    elif "What is your purpose" in command:
        speak("I am virtual assitant and I was made for Iron Man suit in real life. It looks like joke but me and sir aditya made the 99 percent achievement in successful testing of nanobots. so dreams comes true in few time. wait watch.")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("I'm sorry, I don't know how to respond to that.")

    return True

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your virtual assistant. How can I help you?")
    while True:
        command = listen_for_command()
        if not respond_to_command(command):
            break
