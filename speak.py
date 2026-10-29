# Mouth of the jarvis
import pyttsx3

def speak(text):
    # Create a new engine for every call, so it never gets stuck after the first one.
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()