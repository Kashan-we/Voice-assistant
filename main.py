import speech_recognition as sr
import webbrowser
import subprocess
import musicLibrary
import requests

recognizer = sr.Recognizer()

newsapi = "2776a6a492de4de788fb991da3db6bd6"


def speak(text):
    powershell_script = """
    Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $text = [Console]::In.ReadToEnd()
    $speak.Speak($text)
    """

    subprocess.run(
        ["powershell", "-NoProfile", "-Command", powershell_script],
        input=text,
        text=True
    )


def processCommand(c):
    print("Command received:", c)

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open whatsapp" in c.lower():
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        speak(f"Playing {song}")
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        speak("Opening news")

    try:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}",
            timeout=10
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if articles:
                for article in articles[:5]:
                    headline = article.get("title")

                    if headline:
                        print("Headline:", headline)
                        speak(headline)
            
                

        else:
            print("News API Error:", r.status_code)
            speak("Sorry, I could not fetch the news")

    except Exception as e:
        print("News Error:", e)
        speak("Sorry, there was an error fetching the news")


if __name__ == "__main__":
    speak("Initializing.......................... Say Ultron to activate me..")

    while True:
        r = sr.Recognizer()

        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")

                audio = r.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=1
                )

            word = r.recognize_google(audio)
            print("You said:", word)

            if word.lower() == "ultron":
                speak("Ultron Awakening, Plese give me command")

                with sr.Microphone() as source:
                    print("Ultron here ..")

                    audio = r.listen(source)

                command = r.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", type(e).__name__, ":", e)