import webbrowser
from musicLibrary import get_song_link
from speak import speak 

WEBSITES = {
    "youtube": ("Opening YouTube.", "https://youtube.com"),
    "google": ("Opening Google.", "https://google.com"),
    "linkedin": ("Opening LinkedIn.", "https://www.linkedin.com/in/richabenmakwana/"),
    "facebook": ("Opening Facebook.", "https://www.facebook.com/"),
    "chatgpt": ("Opening ChatGPT.", "https://chatgpt.com/"),
    "instagram": ("Opening Instagram.", "https://www.instagram.com/"),
    "github": ("Opening GitHub.", "https://github.com/"),
}

EXIT_WORDS = ["stop", "exit", "goodbye", "bye", "quit"]
def process_command(command):
    if command == "":
        speak("Sorry, I did not catch that.")
        return True
    
    if command.startswith("play"):
         song = command.replace("play", "", 1).strip()
         if song == "":
            speak("Which song should I play?")
         else:
            speak(f"Playing {song}.")
            webbrowser.open(get_song_link(song))
         return True
      
    if any(word in command for word in EXIT_WORDS):
        speak("Goodbye! Have a great day.")
        return False

    for name, (message, link) in WEBSITES.items():
        if name in command:
            speak(message)
            webbrowser.open(link)
            return True

    speak("Sorry, I don't know that command yet.")
    return True