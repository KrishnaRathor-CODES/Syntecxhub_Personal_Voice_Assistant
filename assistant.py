import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import random
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
user_name = "friend"
last_url = "https://www.google.com"

def talk(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            return query.lower()
        except Exception:
            return ""

def greet_user():
    global user_name
    hour = datetime.datetime.now().hour
    if hour < 12: greeting = "Good morning"
    elif 12 <= hour < 18: greeting = "Good afternoon"
    else: greeting = "Good evening"
    
    talk(f"{greeting}. I am your personal assistant. What is your name?")
    name_check = listen()
    if name_check:
        user_name = name_check.split()[-1]
    talk(f"Nice to meet you, {user_name}. How can I help you today?")

def process_command():
    global last_url
    cmd = listen()
    if not cmd: return
    
    personal = random.choice([f" {user_name}", ""])
    
    if "time" in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {now}{personal}.")
    
    elif "open google" in cmd:
        last_url = "https://www.google.com"
        webbrowser.open(last_url)
        talk(f"Opening Google now{personal}.")
        
    elif "open youtube" in cmd:
        last_url = "https://www.youtube.com"
        webbrowser.open(last_url)
        talk("Loading YouTube.")
        
    elif "search for" in cmd:
        term = cmd.replace("search for", "").strip()
        last_url = f"https://www.google.com/search?q={term}"
        webbrowser.open(last_url)
        talk(f"Searching for {term} on the web.")

    elif "open chrome" in cmd or "open browser" in cmd:
        webbrowser.open("https://www.google.com")
        talk("Opening your browser.")

    elif "open it" in cmd:
        webbrowser.open(last_url)
        talk(f"Opening that last link again for you{personal}.")

    elif "how are you" in cmd:
        talk(random.choice(["I'm doing great, thanks for asking!", "I'm feeling wonderful today!", "Systems are optimal and I'm ready to help!"]))

    elif "who are you" in cmd:
        talk(random.choice(["I'm your custom Python assistant.", "I am a simple AI built to make your life easier.", "I'm your digital buddy."]))

    elif "thank you" in cmd or "thanks" in cmd:
        talk(random.choice(["You are very welcome!", "No problem at all!", "Glad I could help.", f"Anytime{personal}!"]))

    elif "what can you do" in cmd or "help" in cmd:
        talk("I can tell you the time, search Google, open YouTube, tell jokes, and have a little chat!")

    elif "are you real" in cmd:
        talk(random.choice(["I am as real as the code that runs me.", "I exist in the digital world.", "I'm real enough to talk to you!"]))

    elif "joke" in cmd:
        talk(random.choice(["Why did the programmer quit? Because he didn't get arrays.", "What do you call a fake noodle? An impasta.", "I'm afraid for the calendar. Its days are numbered."]))

    elif "awesome" in cmd or "good job" in cmd:
        talk(random.choice(["I appreciate the compliment!", f"Thanks{personal}, you're pretty great too!", "I try my best!"]))

    elif any(word in cmd for word in ["exit", "bye", "stop"]):
        talk(f"Goodbye {user_name}! Have a great day.")
        sys.exit()

    else:
        talk(random.choice(["I'm sorry, I didn't quite catch that.", "Could you say that again?", "I'm not sure how to help with that yet."]))

if __name__ == "__main__":
    greet_user()
    while True:
        process_command()