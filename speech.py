# Ears of the jarvis
import speech_recognition as sr

def take_command():
  recognizer = sr.Recognizer()  

  with sr.Microphone() as source:
    print("Listening....")
    audio = recognizer.listen(source)

  try:
    command = recognizer.recognize_google(audio)
    return command.lower()
  
  except Exception:
    return ""

