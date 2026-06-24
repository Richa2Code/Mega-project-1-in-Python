import webbrowser
from speak import speak 
def process_command(command):
    if "youtube" in command:
      speak("opening the youtube !.")
      webbrowser.open("https://youtube.com")
    elif "google" in command:
      speak("opening the Google !.")
      webbrowser.open("https://google.com")
    elif "linkedin" in command:
       speak("Opening the linkdin !.")
       webbrowser.open("https://www.linkedin.com/in/richabenmakwana/")
    elif "facebook" in command:
       speak("Opening the Facebook.")
       webbrowser.open("https://www.facebook.com/")
    elif "chatgpt" in command:
       speak("Opening the ChatGPT.")
       webbrowser.open("https://chatgpt.com/")
    elif "instagram" in command:
       speak("Opening the instagram.")
       webbrowser.open("https://www.instagram.com/")
    elif "github" in command:
       speak("Opening the GitHub.")
       webbrowser.open("https://github.com/")