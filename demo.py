import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice speed & volume
engine.setProperty("rate", 180)   # speed of speech
engine.setProperty("volume", 1.0) # volume (0.0 to 1.0)

def speak(text):
    """Make Jarvis speak"""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice commands and return as text"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # reduce noise
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Didn't catch that.")
            return ""
        except sr.RequestError:
            print("Internet issue.")
            return ""

def activate_jarvis():
    """Wait for 'Jarvis' hotword to activate"""
    while True:
        command = listen()
        if "jarvis" in command:
            speak("How may I help you sir?")
            handle_commands()

def handle_commands():
    """Handle commands once Jarvis is active"""
    while True:
        command = listen()

        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "play music" in command:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("What do you want me to search, sir?")

        elif "what time is it" in command or "tell me the time" in command:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye sir")
            break

        else:
            speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    speak("Jarvis online. Say my name to activate me.")
    time.sleep(1)
    activate_jarvis()
