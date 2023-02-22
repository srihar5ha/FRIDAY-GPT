import speech_recognition as sr

class GetInputfromUser:
    
    def __init__(self):
        self.recognizer=sr.Recognizer()

    def get_audio_input(self):
        with sr.Microphone() as source:
            print("Speak now")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source,timeout=5)
            return audio

    def recognize_speech(self):
        audio = self.get_audio_input()
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Unable to recognize your speech")
        except sr.RequestError as e:
            print("Request error: ", e)
    