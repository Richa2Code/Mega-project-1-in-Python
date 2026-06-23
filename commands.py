import webbrowser
from speak import speak 
def process_command(command):
    if "youtube" in command:
        engine.say("Opening the youtube")
        engine.runandwait()
        webbrowser.open("https://youtube.com")