from speech import take_command
from speak import speak
from commands import process_command

speak("Jarvis is online. Say Jarvis to wake me up.")

running = True

GREETINGS = ["hello", "hey", "hi", "ok", "okay"]
while running:

    text = take_command()

    if "jarvis" in text:
        # If you said "jarvis open youtube" in one go, use the rest as the command.
        words = text.replace("jarvis", "").split()
        command = " ".join(w for w in words if w not in GREETINGS)

        # If you only said "jarvis", ask and listen again.
        if command == "":
            speak("Yes, how may I help you today?")
            command = take_command()

        running = process_command(command)