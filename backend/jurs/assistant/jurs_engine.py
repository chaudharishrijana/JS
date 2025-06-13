# assistant/jurs_engine.py
import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    print(f"JURS says: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        speak("Could not request results from speech service.")
        return ""

def wait_for_wake_word(wake_word="srijana"):
    while True:
        print("Waiting for wake word...")
        text = listen()
        if wake_word in text:
            return True
        else:
            print(f"Wake word '{wake_word}' not detected.")

def process_command(command):
    print(f"Processing command: {command}")
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    else:
        speak("Sorry, I don't understand that command.")

def main():
    speak("Initializing JURS...")
    while True:
        activated = wait_for_wake_word("srijana")
        if activated:
            speak("Yes? What should I do?")
            command = listen()
            if command:
                process_command(command)

if __name__ == "__main__":
    main()
