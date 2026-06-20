# Ears of the jarvis
import speech_recognition as sr

def take_command():
  recongnizer = sr.Recognizer()  

  with sr.Microphone() as source:
    print("Listening....")
    audio = recongnizer.listen(source)

  try:
    command = recongnizer.recognize_google(audio)
    return command.lower()
  
  except Exception:
    return ""

