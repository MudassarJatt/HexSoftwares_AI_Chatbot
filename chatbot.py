import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name ?", ["I am your AI chatbot."]],
    [r"how are you ?", ["I am fine, thank you!", "Doing great!"]],
    [r"sorry (.*)", ["No problem!", "It's okay."]],
    [r"i am (.*)", ["Nice to meet you %1"]],
    [r"quit", ["Bye! Take care."]]
]

chatbot = Chat(pairs, reflections)

print("Hi! I am your chatbot. Type 'quit' to exit.")
chatbot.converse()