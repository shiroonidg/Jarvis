import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time

# Initialize recognizer & TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input & convert to text"""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=5)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sir, I am unable to connect to the internet.")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def activate_jarvis():
    """Wait for wake-word 'Jarvis'"""
    speak("Jarvis online. Say 'Jarvis' to activate me.")

    while True:
        command = listen()

        if "jarvis" in command:
            speak("Yes sir?")
            handle_commands()

        time.sleep(0.3)  # prevent endless CPU loop

def handle_commands():
    """Handle tasks after activation"""
    while True:
        command = listen()

        if not command:
            continue

        # Commands
        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "play music" in command:
            speak("Playing music on Spotify")
            webbrowser.open("https://open.spotify.com")

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("What do you want me to search, sir?")

        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "stop" in command or "exit" in command or "sleep" in command:
            speak("Going to sleep, sir.")
            break

        else:
            speak("I didn't get that sir. Please say it again.")

if __name__ == "__main__":
    activate_jarvis()



        

    