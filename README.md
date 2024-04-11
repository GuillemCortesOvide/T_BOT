
# T-Bot: The Ticket Chatbot

## Overview

T-Bot is a chatbot designed to streamline communication by retriving tickets or tasks from your kanban board. This repository houses the codebase for T-Bot, showcasing its capabilities in handling user queries and facilitating task management.

## Features

- **Logic Response**: T-Bot utilizes a set of functions that focus on getting the user input on from the variable responses then checks the probability from user input and replies with the corresponding response from the list.
- **Integration with Trello**: T-Bot in this case integrates with Trello boards, allowing users to fetch the the existing tickets from trello within the chat. You can use another tool like JIRA, just make sure to replace the values on keys.py and the api URL on api_requests.py.

## Usage

To interact with T-Bot, simply run the provided Python script and start typing your queries. T-Bot will analyze your input and provide relevant responses based on predefined keywords and message probabilities. You can add more complex responses by adding more key values pairs on the lists assigned on the variable responses.

## How to Run

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Ensure you have valid API keys for Trello (replace placeholders with your actual keys in `keys.py`).
4. Execute the main script by running `python chatbot.py`.
5. Start interacting with T-Bot!

## Future Improvements

- **Enhanced Natural Language Understanding**: Continuously improve T-Bot's ability to understand and respond to user queries with higher accuracy.
- **Extended Integration Support**: Integrate T-Bot with additional project management tools and platforms to expand its functionality.
- **Performance Optimization**: Optimize T-Bot's response time and resource utilization for better scalability.

## About the Author

This project is maintained by Guillem Cortés Ovide. Feel free to reach out with any inquiries or suggestions.

