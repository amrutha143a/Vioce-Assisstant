
import speech_recognition 
import pyttsx3
import datetime
import wikipedia
import webbrowser



def speak(text):
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.say(text)
  engine.runAndWait()

def takeCommand():
  r = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

  except Exception as e:
    # print(e)
    speak("Say that again")
    return "None"
  return query

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")

  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")

  else:
    speak("Good Evening!")

  speak("I am Ammu . How may I help you?")

def time():
  Time = datetime.datetime.now().strftime("%H:%M:%S")
  speak(f"The current time is {Time}")

def date():
  year = int(datetime.datetime.now().year)
  month = int(datetime.datetime.now().month)
  day = int(datetime.datetime.now().day)
  speak(f"Today is {day} {month} {year}")

def wikipedia_search(query):
  speak("Searching Wikipedia...")
  try:
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)
  except Exception as e:
    speak("Sorry, I couldn't find that.")

def search_web(query):
  speak("Searching the web...")
  webbrowser.open(f"https://www.google.com/search?q={query}")



if __name__ == "__main__":
  wishMe()
  while True:
    query = takeCommand().lower()

    if 'time' in query:
      time()

    elif 'date' in query:
      date()

    elif 'wikipedia' in query:
      query = query.replace("wikipedia", "")
      wikipedia_search(query)

    elif 'search' in query:
      query = query.replace("search", "")
      search_web(query)

    elif 'hello' in query:
      speak("Hello there! How can I help you?")
