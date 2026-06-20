import pyttsx3

# init means start engine and h created engine will be stored in a variable named engine.
engine = pyttsx3.init()

# function that takes text as parameter to speak.
def speak(text):
    # thi sis method which tells the engine to prepare itself to speak this text.
    engine.say(text)

    # it tells now start speaking and wait untill speech finishes
    engine.runAndWait()