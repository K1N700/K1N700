import telebot

CHAVE_API ="chave"

bot= telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Ruim"])
def Ruim(mensagem):
    bot.send_message(mensagem.chat.id , "Sabemos que vc tbm é Ruim")

@bot.message_handler(commands=["Regular"])
def Regular(mensagem):
    bot.send_message(mensagem.chat.id, "Sabemos que vc tbm é Regular")

@bot.message_handler(commands=["Bom"])
def Bom(mensagem):
    bot.send_message(mensagem.chat.id, "Sabemos que vc tbm é Bom")

@bot.message_handler(commands=["Otimo"])
def Otimo(mensagem):
    bot.send_message(mensagem.chat.id, "Sabemos que vc tbm é Ótimo")

@bot.message_handler(commands=["Exelente"])
def Exelente(mensagem):
    bot.send_message(mensagem.chat.id, "Sabemos que vc tbm é Exelente")



@bot.message_handler(commands=["Opicao1"])
def opicao1(mensagem):
    texto2="""
    Como foi a sua experiência em jogar e visitar meu site:
    /Ruim  
    /Regular  
    /Bom  
    /Otimo  
    /Exelente
    """
    bot.send_message(mensagem.chat.id, texto2)

@bot.message_handler(commands=["Opicao2"])
def opicao2(mensagem):
    bot.send_message(mensagem.chat.id , "Clique aqui ->https://portfoliomarcos.netlify.app/<- e fale com o Marcos")


@bot.message_handler(commands=["Opicao3"])
def opicao3(mensagem):
    bot.send_message(mensagem.chat.id , "Oi vc pode ajudar mandando R$2,00 pra esse PIX 21991304806 Tel")

###########################################################################################################################

def verificar(mensagem):
    return True



@bot.message_handler(func=verificar)
def responder(menssagem):
    text ="""
Escolhe ai:

/Opicao1 Classificar meu site e jogos
/Opicao2 Cotar um serviço
/Opicao3 Apoiar meus projetos 

O chat não responde outras perguntas, não insista.
Clique nas opções.
    
    """
    bot.reply_to(menssagem, text)

bot.polling()
