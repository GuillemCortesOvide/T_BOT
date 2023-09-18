import keys
import requests


api_key = keys.TRELLO_API_KEY
api_url = 'https://api.trello.com/1/boards/64c9044d7f1bb7fc6d52bb47/cards?key=0fdb0e3559eb74018decd37b1f6f88d5&token=ATTA385cd45d90e87e0d79da75defcb3ae0c5afce6f19dcff8edba799bc6794e10334BA99AA6'

def getdata():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an exception for non-200 status codes
        json_data = response.json()
        print(json_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
