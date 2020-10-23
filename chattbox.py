from chatterbot.trainers import ListTrainer #Método para treinar o chatbot
from chatterbot import ChatBot


bot = ChatBot('Test') #create the chatbot

conversa = ['Oi','Olá','Tudo bem ?', 'Eu estou bem']

bot.set_trainer(ListTrainer)

bot.train(conversa)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ', response)