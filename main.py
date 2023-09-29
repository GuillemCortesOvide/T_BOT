import re
import requests
import long_responses as long
from keys import TRELLO_API_KEY, TRELLO_TOKEN

# Define the responses and their associated information
responses = [
    {
        "text": "I'm T-Bot, your ticket chatbot! What can I help you for?",
        "keywords": ["hello", "hola", "hey", "hi"]
    },
    {
        "text": "I'm doing fine, and you?",
        "keywords": ["how", "are", "you", "doing"]
    },
    {
        "text": "You're Welcome",
        "keywords": ['Thanks', 'Thank you']
    },
    {
        "text": 'Sure:',
        "keywords": ['Can', 'you', 'show', 'me', 'the', 'tickets']
    }
]

highest_prob_list = {}

def get_response(user_input):
    split_message = re.split(r'\s+|,;?!.-]/s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognised_words):
    message_certainty = 0

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = (message_certainty / len(recognised_words)) * 100
    return int(percentage)


def check_all_messages(message):
    for response in responses:
        message_certainty = message_probability(message, response["keywords"])
        if message_certainty > 0:
            highest_prob_list[response["text"]] = message_certainty

            if response["text"] == 'Sure:':
                cards_data = get_trello_cards()
                if cards_data:
                    card_names = [card['name'] for card in cards_data]
                    cards_response = "Here are the cards:\n" + "\n".join(card_names)
                    return cards_response
                else:
                    return "No cards found."
            else:
                return response["text"]

    return long.unknown()


def get_trello_cards():
    api_url = f"https://api.trello.com/1/boards/64c9044d7f1bb7fc6d52bb47/cards?key={TRELLO_API_KEY}&token={TRELLO_TOKEN}"
    response = requests.get(api_url)
    if response.status_code == 200:
        cards_data = response.json()
        return cards_data
    else:
        print("Sorry, failed to fetch cards:", response.text)
    return []


def close_bot():
    print("Tbot: Good Bye! See you soon.")
    exit()

if __name__ == "__main__":
    while True:
        user_input = input('You: ')
        if "bye" in user_input.lower():
            close_bot()
        else:
            print('Tbot: ' + get_response(user_input))
