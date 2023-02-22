import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source of input
with sr.Microphone() as source:
    print("Speak now:")
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # listen for user's input
    audio = r.listen(source)

# recognize the user's input
try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Unable to recognize your speech")
except sr.RequestError as e:
    print("Request error: ", e)
