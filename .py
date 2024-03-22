import random
import nltk
from nltk.chat.util import Chat, reflections

# Define reflections for pronoun conversion
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define chatbot responses
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi there! How can I help you?"],
    "information": ["What specific information do you need?", "Please specify the information you are looking for."],
    "queries": ["Feel free to ask any questions you have.", "I'm here to help with your queries."],
    "navigation": ["Are you looking for help with navigating specific systems or platforms?", "Navigating college systems can be complex. Let me know how I can assist you."],
    "default": ["I'm sorry, I don't understand. Can you please rephrase?", "Could you provide more context or be more specific?"]
}

# Create a Chat instance
chatbot = Chat(responses, reflections)

# Main interaction loop
print("Welcome to College Chatbot! How can I assist you?")
print("You can type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day.")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
