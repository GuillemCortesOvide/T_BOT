import random


def unknown():
    response = ['I did not understand, could you repeat and avoid typos please?',
                "Hmm...",
                "Okay, but you think this is related with tickets?",
                "What does that mean? Remember that I'm Tbot a Chatbot ticket", "Pardon me?",
                "Remember, if you want to know about tickets just say the word 'Tickets' "][random.randrange(6)]
    return response