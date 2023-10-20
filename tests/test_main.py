# test_chatbot.py

import chatbot_py


def test_message_probability():
    user_message = ['hello']
    recognised_words = ['hello', 'hey', 'hi']
    result = chatbot_py.message_probability(user_message, recognised_words)
    assert result == 33


def test_check_all_messages():
    message = ['hello']
    result = chatbot_py.check_all_messages(message)
    assert result == "I'm T-Bot, your ticket chatbot! What can I help you with?"


def test_get_trello_cards(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        return MockResponse(200, [{"name": "Card 1"}, {"name": "Card 2"}])

    monkeypatch.setattr('requests.get', mock_get)

    result = chatbot_py.get_trello_cards()
    assert result == [{"name": "Card 1"}, {"name": "Card 2"}]


def test_get_response():
    user_input = "hello"
    result = chatbot_py.get_response(user_input)
    assert result == "I'm T-Bot, your ticket chatbot! What can I help you with?"
