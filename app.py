import source.user_input as user_input
import source.davinci_output as davinci_output
import os
import pyttsx3

def main():

    input_obj=user_input.GetInputfromUser()
    api_key = os.getenv("OPENAI_API_KEY")
    print("started ",api_key)
    #user_audio=input_obj.get_audio_input()
    user_query=input_obj.recognize_speech()
    print("user query is ",user_query)
    output_obj=davinci_output.Davinci_api()
    output_obj.prompt=user_query
    davinci_response=output_obj.get_response(api_key=api_key)
    print("davinci response is ",davinci_response.choices[0].text.strip())
    #for choice in davinci_response.choices:
     #   print(choice.text.strip())



    engine = pyttsx3.init()

    # Set the voice rate
    engine.setProperty('rate', 150)

    #Set the voice properties for a natural-sounding voice
    voices = engine.getProperty('voices')
    voice = voices[1]  # Choose voice with index 1 for a natural-sounding voice
    engine.setProperty('voice', voice.id)
    engine.setProperty('volume', 1.0)
    engine.setProperty('pitch', 1.0)
    engine.say(davinci_response.choices[0].text.strip())
    engine.runAndWait()



if __name__=="__main__":
    main()