import speech_recognition as sr

listener = sr.Recognizer()

wake = 'computer'

try:
    with sr.Microphone() as source:
      print("listening")  
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      command = command.lower()
      if wake in command:
        print(command)
except Exception as e:
    print(f"{e} exception occured")
