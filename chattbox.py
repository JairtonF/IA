from chatterbot.trainers import ListTrainer #Método para treinar o chatbot
from chatterbot import ChatBot
import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

while True:
    request = input("You: ")
    response = kernel.respond(request)

    print("Bot: ", response)