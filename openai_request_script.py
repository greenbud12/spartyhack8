import os
import requests
import json

def send_request(text_message):
    # Define the API endpoint and your API key
    api_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/completions"
    api_key = os.environ["OPENAI_API_KEY"]

    # Define the input parameters for the API request
    data = {
        "prompt": text_message,
        "temperature": 0.5,
        "max_tokens": 128,
    }

    # Make the API request
    response = requests.post(api_endpoint, json=data, headers={ "Authorization": f"Bearer {api_key}"})

    # Print the response
    data = json.dumps(response.json(), indent=4)

    # Edit response for sending
    text = ""
    temp = response.json()
    if "choices" in temp:
        choices = temp["choices"][0]
        if "text" in choices:
            text = choices["text"]

            if "finish_reason" in choices:
                finish_reason = choices["finish_reason"]
                if finish_reason == "length":
                    text = text + "\n\nDue to testing response was cut short to cost less."
                if finish_reason == "stop":
                    pass # succsessful full response
                else:
                    print("REASON NOT ACCOUNTED FOR:", finish_reason)
            
    # response for user
    return text


