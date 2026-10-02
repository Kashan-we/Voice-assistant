# 🤖 Jarvis – Python Voice Assistant

Jarvis is a **Python-based voice assistant** that listens for a wake word, understands voice commands, and performs different tasks such as opening websites, playing music, and fetching the latest news.

This project is being developed as a learning project to understand **Python, Speech Recognition, APIs, automation, and voice-based applications**. The goal is to gradually turn Jarvis into a more advanced AI assistant by adding features such as **OpenAI integration, natural-language conversations, task automation, and more**.

---

## 🚀 Features

### 🎙️ Voice Activation

Jarvis continuously listens for the wake word:

> **"Jarvis"**

Once activated, it listens for the user's command.

### 🌐 Website Opening

Jarvis can open commonly used websites through voice commands:

* Google
* YouTube
* LinkedIn
* Facebook
* Instagram
* WhatsApp

Example:

```text
Jarvis
→ Open Google
```

Jarvis responds:

```text
Opening Google
```

and opens the website automatically.

### 🎵 Music Playback

Jarvis can play songs using links stored in a separate `musicLibrary.py` file.

Example:

```text
Jarvis
→ Play <song>
```

The assistant searches the song in the music library and opens its corresponding link in the browser.

### 📰 News Fetching

Jarvis uses the **NewsAPI** to retrieve current headlines.

When the user says:

```text
Jarvis
→ News
```

Jarvis requests the latest Indian headlines from NewsAPI and reads the available headlines using Windows text-to-speech.

### 🔊 Text-to-Speech

Jarvis uses **Windows PowerShell's System.Speech** engine to convert text into spoken audio.

This allows Jarvis to respond verbally instead of only displaying text in the terminal.

### 🎤 Speech Recognition

The project uses the Python `SpeechRecognition` library with Google's speech recognition service to convert the user's voice into text.

---

# 🛠️ Technologies Used

| Technology                | Purpose                             |
| ------------------------- | ----------------------------------- |
| Python                    | Main programming language           |
| SpeechRecognition         | Converts speech into text           |
| Google Speech Recognition | Processes voice input               |
| PyAudio                   | Captures microphone audio           |
| Requests                  | Sends requests to NewsAPI           |
| NewsAPI                   | Provides news headlines             |
| Webbrowser                | Opens websites                      |
| PowerShell System.Speech  | Converts text to speech             |
| Git & GitHub              | Version control and project hosting |

---

# 📂 Project Structure

The project can be organized like this:

```text
Jarvis/
│
├── main.py
├── musicLibrary.py
├── README.md
└── .venv/
```

### `main.py`

Contains the main Jarvis program, including:

* Speech recognition
* Voice activation
* Command processing
* Website opening
* Music playback
* News fetching
* Text-to-speech

### `musicLibrary.py`

Contains the music dictionary used by Jarvis to find and play songs.

Example structure:

```python
music = {
    "song1": "https://example.com/song1",
    "song2": "https://example.com/song2"
}
```

### `.venv`

Python virtual environment used to keep the project's dependencies isolated from the system Python installation.

---

# ⚙️ How Jarvis Works

The basic working process is:

```text
             ┌─────────────────┐
             │     Start       │
             └────────┬────────┘
                      ↓
             ┌─────────────────┐
             │ Listen for      │
             │ "Jarvis"        │
             └────────┬────────┘
                      ↓
             ┌─────────────────┐
             │ Speech          │
             │ Recognition     │
             └────────┬────────┘
                      ↓
              Is it "Jarvis"?
                 /          \
               No            Yes
               ↓              ↓
        Keep listening   Activate Jarvis
                              ↓
                     Listen for command
                              ↓
                     Convert speech to text
                              ↓
                       Process command
                              ↓
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
          Website          Music            News
              ↓               ↓               ↓
          Open URL       Open song link   Fetch headlines
                                              ↓
                                         Speak headlines
```

---

# 💻 Installation

## 1. Install Python

Download and install Python from the official Python website.

During installation, make sure to enable:

```text
Add Python to PATH
```

You can verify the installation with:

```bash
python --version
```

or:

```bash
py --version
```

---

## 2. Clone the Repository

Clone the project using Git:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd Jarvis
```

---

# 🧪 3. Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Git Bash:

```bash
source .venv/Scripts/activate
```

After activation, you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal.

---

# 📦 4. Install Required Packages

Install the required Python libraries:

```bash
pip install SpeechRecognition
pip install PyAudio
pip install requests
```

You can also install them together:

```bash
pip install SpeechRecognition PyAudio requests
```

---

# 🔑 5. Configure NewsAPI

Jarvis uses NewsAPI to retrieve news headlines.

Create an account on NewsAPI and obtain an API key.

Then add your API key to `main.py`:

```python
newsapi = "YOUR_NEWSAPI_KEY"
```

### ⚠️ Important

Do **not** upload your real API key to GitHub.

Instead, use an environment variable or a separate configuration file that is excluded using `.gitignore`.

For example:

```text
.env
```

should be added to:

```text
.gitignore
```

---

# 🎵 6. Configure Music Library

Create or edit:

```text
musicLibrary.py
```

Example:

```python
music = {
    "believer": "SONG_URL",
    "shape": "SONG_URL",
    "faded": "SONG_URL"
}
```

The command:

```text
Jarvis
→ Play believer
```

will search for `"believer"` in the music dictionary and open its corresponding URL.

---

# ▶️ Running Jarvis

After activating the virtual environment, run:

```bash
python main.py
```

Jarvis will start with:

```text
Initializing Jarvis
```

The assistant will then wait for the wake word.

Say:

```text
Jarvis
```

Jarvis will respond:

```text
Yes sir, I am listening
```

You can then give a command.

---

# 🗣️ Example Commands

### Open Google

```text
Jarvis
Open Google
```

### Open YouTube

```text
Jarvis
Open YouTube
```

### Open Instagram

```text
Jarvis
Open Instagram
```

### Play Music

```text
Jarvis
Play believer
```

### Get News

```text
Jarvis
News
```

Jarvis will fetch the available headlines and read them aloud.

---

# 🧠 How the Code Is Built

The project is divided into several logical components.

## 1. Speech Recognition

```python
recognize_google()
```

is used to convert the microphone input into text.

The assistant first listens for:

```text
Jarvis
```

and then listens for the actual command.

---

## 2. Command Processing

The function:

```python
processCommand(c)
```

handles the user's commands.

For example:

```python
if "open google" in c.lower():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")
```

This checks the recognized command and performs the appropriate action.

---

## 3. Text-to-Speech

The `speak()` function uses Windows PowerShell:

```text
System.Speech.Synthesis.SpeechSynthesizer
```

to convert text into speech.

This allows Jarvis to provide audible responses.

---

## 4. News API

The `requests` library sends an HTTP request to NewsAPI:

```python
requests.get(...)
```

The returned JSON data is then processed to extract article titles.

---

# 🔮 Future Improvements

This project is currently in development. The long-term goal is to transform Jarvis from a basic command-based voice assistant into a more capable AI assistant.

### 🤖 OpenAI Integration

An upcoming version will integrate an AI model so Jarvis can understand natural-language questions and have more meaningful conversations.

For example:

```text
Jarvis, explain recursion in Python.
```

Instead of only recognizing predefined commands, Jarvis will be able to process the request and generate an appropriate response.

### Planned Features

* 🤖 OpenAI API integration
* 💬 Natural-language conversations
* 🧠 AI-powered question answering
* 🌐 Web search
* 📧 Email automation
* 📅 Calendar integration
* 📁 File and folder automation
* 💻 System control
* 🔍 Better command understanding
* 🎙️ Improved voice recognition
* 🗣️ More natural voice responses
* 🔐 Secure API-key management
* 🧩 Modular command system
* ⚡ Faster command execution
* 🪟 GUI interface
* 🧠 Context-aware conversations

---

# 📈 Project Roadmap

```text
Phase 1
│
├── Python fundamentals
├── Speech recognition
├── Text-to-speech
└── Basic commands
        ↓
Phase 2
│
├── Website automation
├── Music system
├── News API
└── Better error handling
        ↓
Phase 3
│
├── OpenAI integration
├── Natural-language processing
└── AI conversations
        ↓
Phase 4
│
├── System automation
├── Web search
├── File management
└── External APIs
        ↓
Phase 5
│
├── GUI
├── Context/memory
├── Modular architecture
└── Advanced AI assistant
```

---

# 🐛 Error Handling

The project includes exception handling so that unexpected errors do not immediately terminate the assistant.

For example:

```python
try:
    ...
except Exception as e:
    print("Error:", e)
```

This helps identify problems during development and testing.

---

# 🔐 Security

If you fork or clone this project, make sure you **never commit API keys, passwords, tokens, or other secrets** to GitHub.

Use environment variables for sensitive information as the project becomes more advanced.

---

# 🎯 Project Goal

The main goal of this project is to build Jarvis step-by-step while learning how different technologies work together.

The project started as a simple Python voice assistant and is intended to evolve into a more advanced AI-powered personal assistant.

```text
Python Voice Assistant
        ↓
Automation
        ↓
API Integration
        ↓
AI Integration
        ↓
Advanced Personal Assistant
```

---

# 👨‍💻 Author

**Abdul Hayi**

B.Tech Computer Science Engineering Student

Interested in:

* Python
* Web Development
* Artificial Intelligence
* Automation
* Software Development

---

# ⭐ Contributing

This project is primarily a learning project, but suggestions, improvements, and ideas are welcome.

If you find an issue or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# 📜 License

This project is intended for educational and learning purposes.
