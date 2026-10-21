import pyttsx3

try:
    text = input("Enter the text you want to convert to speech: ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Retrieve the available system voices
    voices = engine.getProperty('voices')

    # Set the voice to male
    # On Windows, voices[0].id is usually the default male voice (e.g., "David")
    # On macOS, voices[0].id is usually a male voice (e.g., "Alex")
    engine.setProperty('voice', voices[0].id)

    # Save the output to an audio file
    engine.save_to_file(text, 'Output.mp3')

    # Execute the saving process
    engine.runAndWait()
except Exception as e:
    print(f"An error occurred: {e}")