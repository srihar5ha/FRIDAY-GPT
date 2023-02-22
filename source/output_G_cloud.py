from google.cloud import texttospeech

# Set up a client
client = texttospeech.TextToSpeechClient()

# Set the text input
text = "Hello, welcome to Friday-GPT!"
synthesis_input = texttospeech.SynthesisInput(text=text)

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-D",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Set the audio file format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio response to a file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
