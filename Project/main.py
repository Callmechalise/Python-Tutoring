#pip install requests
import requests

word = input("Enter a word: ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url)
data = response.json()
meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
print("Meaning:", meaning)