Text-to-Speech Audio Generator

A simple Python script that converts text input into spoken audio and saves it as an MP3 file. This project uses the pyttsx3 library to utilize local system voices, specifically configured to use a male voice.

Prerequisites

Before running the script, ensure you have Python installed on your system. You will also need to install the required pyttsx3 library.

Installation

Clone or download this repository to your local machine.

Open your terminal or command prompt.

Install the required dependency by running:

pip install pyttsx3


Usage

Run the Python script:

python your_script_name.py


When prompted, enter the text you want to convert to speech.

The script will process the text and generate an audio file named Output.mp3 in the same directory.

Troubleshooting Voices

This script defaults to voices[0].id, which is usually a male voice on most operating systems (like "David" on Windows or "Alex" on macOS).

If the generated voice is female or not what you expect, you can change the voice index in the code:

# Try changing voices[0] to voices[1] or voices[2]
engine.setProperty('voice', voices[1].id)


Important Note

The engine.runAndWait() command at the end of the script is essential. It tells the text-to-speech engine to process the queued commands. If this line is removed, the script will execute, but no audio file will be saved.