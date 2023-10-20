import chatbot_py
from chatbot_py import get_response, close_bot

if __name__ == "__main__":
    while True:
        user_input = input('You: ')
        if "bye" in user_input.lower():
            close_bot()
        else:
            print('Tbot: ' + get_response(user_input))
