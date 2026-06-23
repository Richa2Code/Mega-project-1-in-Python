from speech import take_command
from speak import speak
from commands import process_command

while True:

    text = take_command()

    if "jarvis" in text:
        speak("Yes, how may I help you, today?")
    process_command(text)