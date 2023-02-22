import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice rate
engine.setProperty('rate', 150)

# Set the voice properties for a natural-sounding voice
voices = engine.getProperty('voices')
voice = voices[1]  # Choose voice with index 1 for a natural-sounding voice
engine.setProperty('voice', voice.id)
engine.setProperty('volume', 1.0)
engine.setProperty('pitch', 1.0)

# Convert text to speech
text = "Hello, welcome to Friday-GPT!"
engine.say(text)
engine.runAndWait()
