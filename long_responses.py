import random


def unknown():
    response = ['I did not understand, could you repeat and avoid typos please?',
                "Hmm...",
                "Okay, but you think this is related with tickets?",
                "What does that mean? Remember that I'm Tbot a Chatbot ticket"][random.randrange(4)]
    return response