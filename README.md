# Jarvis Voice Assistant

Jarvis is a simple Python-based voice assistant that listens for a wake word and performs specific voice-controlled tasks. The assistant is inspired by the idea of a lightweight desktop AI companion that can help with basic daily actions through speech commands.

The project uses speech recognition for understanding voice input and text-to-speech technology for spoken responses. Once activated with the word “Jarvis”, the assistant can open websites, search Google, play music through Spotify, and tell the current time.

This project was built as a beginner-friendly implementation of voice automation using Python.

---

## Features

Jarvis currently supports a set of predefined commands, including:

- Opening YouTube
- Opening Google
- Opening Spotify
- Searching anything on Google
- Telling the current time
- Voice activation using the wake word “Jarvis”
- Voice responses using text-to-speech

The assistant keeps listening continuously until the stop or exit command is given.

---

## Technologies Used

This project is built using Python and the following libraries:

- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `datetime`
- `time`

---

## How It Works

When the program starts, Jarvis goes into listening mode and waits for the wake word.

Example:

```bash
Jarvis online. Say my name to activate me.
```

## Example commands 

Open YouTube,
Open Google,
Play music,
Search Python tutorials,
What time is it,
Stop


