
# T-Bot: The Ticket Chatbot

## Overview

T-Bot is a chatbot designed to streamline communication by retrieving tickets or tasks from your Kanban board. This repository houses the codebase for T-Bot, showcasing its capabilities in handling user queries and facilitating task management.

## Features

- **Logic Response**: T-Bot utilizes a set of functions that focus on getting the user input from the variable responses then checks the probability from user input and replies with the corresponding response from the list.
- **Integration with Trello**: T-Bot in this case integrates with Trello boards, allowing users to fetch the existing tickets from Trello within the chat. You can use another tool like JIRA, make sure to replace the values on keys.py and the API URL on api_requests.py.

## Usage

To interact with T-Bot, run the provided Python script and start typing your queries. T-Bot will analyze your input and provide relevant responses based on predefined keywords and message probabilities. You can add more complex responses by adding more key-value pairs on the lists assigned to the variable responses.

## How to Run

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Ensure you have valid API keys for Trello (replace placeholders with your actual keys in `keys.py`).
4. Execute the main script by running `python main.py` inside the T_BOT directory.
5. Start interacting with T-Bot!

## About the Author

Guillem Cortés Ovide maintains this project. Feel free to reach out with any inquiries or suggestions.

