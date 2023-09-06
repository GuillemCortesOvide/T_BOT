import re
import requests
import long_responses as long
import keys
from api_requests import getdata

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentatge = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentatge*100)
    else:
        return  0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses --------------------------------------------------------

    response("I'm T-Bot, your ticket chatbot", ["hello", "hola", "hey", "hi"], single_response=True)
    response("I'm doing fine, and you?", ["how", "are", "you", "doing"], required_words=['how', 'are', 'you', 'doing'])

    # Response for fetching Trello cards
    response('Sure, here you have:', ['Can', 'you', 'show', 'me', 'the', 'tickets'], required_words=['show', 'tickets'])

    # ... other responses ...
    def get_cards():
        api_url = f'https://api.trello.com/1/boards/64c9044d7f1bb7fc6d52bb47/cards?key={{TRELLO_API_KEY}}token={{TRELLO_TOKEN}}'
        response = requests.get(api_url)
        if response.status_code == 200:
            cards_data = response.json()
            return cards_data
        else:
            print("Failed to fetch cards:", response.text)
            return []
    # Trello API card retrieval logic
    if highest_prob_list.get('Sure, here you have:', 0) >= 1:
        cards_data = get_cards()
        if cards_data:
            card_names = [card['name'] for card in cards_data]
            cards_response = "Here are the cards:\n" + "\n".join(card_names)
        else:
            cards_response = "No cards found."

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # Return the appropriate response
    if best_match == 'Sure, here are the tickets on the board':
        return cards_response
    else:
        return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def close_bot():
    print("Tbot: Bye bye! See you next time.")
    exit()

def get_response(user_input):
    split_message = re.split(r'\s+|,;?!.-]/s*', user_input.lower())
    response = check_all_messages(split_message)
    return response




if __name__ == "__main__":
    while True:
        user_input = input('You: ')
        if "bye" in user_input.lower():
            close_bot()
        else:
            print('Tbot: ' + get_response(user_input))


