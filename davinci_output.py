
import openai
import os
import requests
import json
#from user_input import user_question

# Initialize the text-to-speech engine

# Set up the API request
#url = "https://api.openai.com/v1/engines/davinci-codex/completions"

#openai.api_key = os.getenv("OPENAI_API_KEY")
#prompt = f"Answer the following question: {user_question}"

# Send the API request
#response = requests.post(url, headers=headers, data=json.dumps(data))


#model_engine = "davinci"

#max_tokens=15
#temperature=0.7
#n=1
#response = openai.Completion.create(
 #   engine=model_engine,
  #  prompt=prompt,
   # temperature=temperature,
    #max_tokens=max_tokens,
#)

#print(response.choices[0].text.strip())


class Davinci_api:

    def __init__(self):
        self.prompt=""
        self.model="text-davinci-003"
        #self.model_engine="davinci"
        self.max_tokens=60
        self.temperature=0.7
        
        #self.openai.api_key = os.getenv("OPENAI_API_KEY")
    def get_response(self,api_key):
        try:
            openai.api_key = api_key
            response=openai.Completion.create(
   model=self.model,
    prompt=self.prompt,
    temperature=self.temperature,
    max_tokens=self.max_tokens,
    top_p=1,
  frequency_penalty=0,
  presence_penalty=0
       )
            #return response.choices[0].text.strip()
            return response
        except :
            print("Connection Error ")




#engine=self.model_engine,
   
#davinci_response=response.choices[0].text.strip()

