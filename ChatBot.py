import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("BotPatins")

conversa = [
    "Olá",
    "Olá, como você está?",
    "Tudo bem e com vc?",
    "Tudo bem, como posso te ajudar?",
    "Estou em busca de informações dos seus produtos",
    "Muito bom, vou te encaminhar nosso catalogo e se tier alguma duvida me chame",
    "Ok, muito obrigado",
    "Eu que agradeço",
    "Posso te ajudar em algo mais?",
    "No momento não, vou analisar o catalogo e se surgir alguma dúvida te chamo aqui ok",
    "Perfeito, estou a disposição"
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

condições_sair = ("sair", "exit", "quit", ":s", ":q")

while True:
    entrada = input("Digite algo para o Jonas: ")
    if entrada in condições_sair:
        break
    else:
        print(f"Jonas: {chatbot.get_response(entrada)}")
