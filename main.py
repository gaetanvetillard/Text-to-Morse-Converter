import requests

API_ENDPOINT =  "https://api.funtranslations.com/translate/morse.json"

text_to_translate = input("Text to translate : \n")
try:
    text = str(text_to_translate)
    params = {
        "text": text
    }
except:
    print("Can't translate that, sorry.")


response = requests.post(API_ENDPOINT, data=params)
data = response.json()

print(data['contents']['translated'])