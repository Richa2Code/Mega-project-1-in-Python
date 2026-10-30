from speech import take_command
from speak import speak
from commands import process_command

GREETINGS = ["hello", "hey", "hi", "ok", "okay"]

# silent listens in a row before Jarvis goes back to sleep
MAX_MISSES = 3          

def clean(text):
    """Remove 'jarvis' and greeting words, keep the real command."""
    words = text.replace("jarvis", "").split()
    return " ".join(w for w in words if w not in GREETINGS)


speak("Jarvis is online. Say Jarvis to wake me up.")

running = True
awake = False      # False = waiting for wake word, True = taking commands
misses = 0

while running:
    text = take_command()

    if not awake:
        # Sleeping: ignore everything until the wake word.
        if "jarvis" in text:
            awake = True
            misses = 0
            command = clean(text)

            if command == "":
                speak("Yes, how may I help you today?")
            else:
                running = process_command(command)

    else:
        # Awake: every sentence is a command, no wake word needed.
        if text == "":
            misses += 1
            if misses >= MAX_MISSES:
                speak("Going back to sleep. Say Jarvis to wake me up.")
                awake = False
            continue

        misses = 0
        command = clean(text)

        if command == "":
            speak("Yes?")
        else:
            running = process_command(command)