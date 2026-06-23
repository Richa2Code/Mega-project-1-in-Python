from speech import take_command
from speak import speak

while True:

    text = take_command()

    if "jarvis" in text:
        speak("Yes, how may I help you, today?")
    process_command(command)