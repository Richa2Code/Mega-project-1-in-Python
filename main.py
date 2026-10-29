from speech import take_command
from speak import speak
from commands import process_command

speak("Jarvis is online. Say Jarvis to wake me up.")

running = True

while running:

    text = take_command()

    if "jarvis" in text:
        # If you said "jarvis open youtube" in one go, use the rest as the command.
        command = text.replace("jarvis", "").strip()

        # If you only said "jarvis", ask and listen again.
        if command == "":
            speak("Yes, how may I help you today?")
            command = take_command()

        running = process_command(command)