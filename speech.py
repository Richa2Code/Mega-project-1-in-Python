# Ears of the jarvis
import speech_recognition as sr

recognizer = sr.Recognizer() 
recognizer.pause_threshold = 0.8 

mic = sr.Microphone()

# Calibrate once, when the program starts. Stay quiet for 1 second.
with mic as source:
    print("Calibrating for background noise, please wait...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

def take_command():
  with mic as source:
        print("Listening....")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            return ""
    
  try:
    command = recognizer.recognize_google(audio, language="en-IN")
    print("You said:", command)
    return command.lower()
  
  except sr.UnknownValueError:
        print("Could not understand")
        return ""
  except sr.RequestError:
        print("Internet problem")
        return ""

