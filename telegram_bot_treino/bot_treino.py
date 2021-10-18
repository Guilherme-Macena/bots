import telebot

TOKEN = '1959821582:AAHL2Ez5E_bHmaX76i8v5z0ozf39jEX16BY'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['Bora'])
def treinar(mensagem):
    inicio = """
       VAMOS NESSA!!!
    
Vai treinar o que hoje?
/Bracos      /Pernas
/Peito      /Costas 
      /Todos
"""

    return bot.reply_to(mensagem, inicio)

@bot.message_handler(commands=['Bracos'])
def treinar_bracos(mensagem):
    pass

@bot.message_handler(commands=['Pernas'])
def treinar_pernas(mensagem):
    pass

@bot.message_handler(commands=['Peito'])
def treinar_peito(mensagem):
    pass

@bot.message_handler(commands=['Costas'])
def treinar_costas(mensagem):
    pass

@bot.message_handler(commands=['Todos'])
def treinar_todos(mensagem):
    pass




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar) #decorator
def responder(mensagem):
    print(mensagem)
    salve = """
    Salvee!!    
    /Bora pro Treino??
    Digite (/Bora) ou clique.
    **Qualquer outra coisa não funciona!**"""
    bot.reply_to(mensagem, salve)


bot.polling()
