from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
import random
import unicodedata
estado_usuario = {}

#função de remoção de remoção de acentos
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

#Função de mensagem de começo do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.from_user.first_name
    await update.message.reply_text(f"Seja bem-vindo(a) {nome} ao Bot da FURIA! Digite /menu para ver o que posso fazer.")

#Função de Menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = (
        "📜 *Menu de Comandos do Bot da Fúria* 📜\n\n"
        "/start - Inicia o bot e dá boas-vindas\n"
        "/menu - Exibe essa lista de comandos\n"
        "/historia - Conheça a trajetória da FURIA\n"
        "/links - Links úteis e redes sociais da FURIA\n"
        "-> Conquistas - Exibe as conquistas da poderosa FURIA\n"
        "-> Jogadores - Exibe a Line-Up atual da FURIA\n"
        "-> Resultados - Saber os resultados dos últimos jogos da FURIA\n"
        "-> Curiosidades - Descubra fatos legais sobre a FURIA\n"
        "-> Bang - Um gifzinho maneiro 😎\n" 
        "-> Granada - Tome cuidado com esse!\n"
        "-> Dance - Sim, eu também sei dançar!\n"
        "-> Melhor Sniper - Bom, você verá o melhor sniper do CS."
    )
    await update.message.reply_text(menu_text, parse_mode="Markdown")

#Coloquei aqui a história da Fúria pois não consegui importar direto de alguma fonte por meio de APIs
async def historia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = remover_acentos(update.message.text.lower())

    if "historia" in mensagem:
    
        texto = (
        "🐾 *História da FURIA Esports* 🐾\n\n"
        "A *FURIA Esports* é uma organização brasileira fundada em *2017*, focada na excelência e inovação nos eSports. "
        "Desde sua criação, a equipe cresceu rapidamente e se destacou em jogos como *CS:GO, League of Legends e Valorant*.\n\n"
        "🔥 Além do desempenho em competições, a FURIA também é reconhecida pelo seu *forte branding* e pelo *engajamento com fãs* ao redor do mundo!"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")



#Função para responder mensagens
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text.lower().lstrip("/")
    nome = update.message.from_user.first_name 
    user_id = update.message.from_user.id

    if "lineup" in mensagem or "jogadores" in mensagem or "line up" in mensagem:
        resposta = (
            "🐾 *Lineup Atual da FURIA CS2 (2025)*\n\n"
            "👑 Gabriel 'FalleN' Toledo – Capitão\n"
            "🔫 Yuri 'yuurih' Santos – Rifler\n"
            "🔫 Kaike 'KSCERATO' Cerato – Rifler\n"
            "🎯 Danil 'molodoy' Golubenko – Sniper\n"
            "🔫 Marek 'YEKINDAR' Galinskis – Rifler\n\n"
            "🎓 Treinador: Sidnei 'sidde' Macedo"
        )
        await update.message.reply_text(resposta, parse_mode="Markdown")
        return
    #Os resultados postos datam até o dia de envio do projeto
    elif "resultados" in mensagem or "último jogo" in mensagem:
        resposta = (
            "*Últimos 3 jogos da Fúria na PGL Bucharest 2025:*\n\n"
            "Fúria 0 - 2 MongolZ\n"
            "Fúria 0 - 2 VP\n"
            "Fúria 1 - 2 COL\n\n"
            "Quaisquer outros resultados, pode encontrar na página da Fúria na Liquipedia pelo */links*"
        )
        await update.message.reply_text(resposta, parse_mode="Markdown")
        return
        
#Aleatorização de curiosidades sobre a FURIA
    
    curiosidades = [
        "A FURIA foi fundada em 2017 e, em apenas dois anos, já estava competindo em um Major, o IEM Katowice 2019.",
        "O time começou com investimento próprio dos fundadores.",
        "A FURIA tem uma Gaming House em Miami, EUA!",
        "Em 2020, a equipe conquistou títulos importantes, como a DreamHack Masters Spring NA, a ESL Pro League Season NA e a IEM New York NA, consolidando-se entre os 10 melhores times do mundo.",
        "A FURIA se tornou uma das principais equipes brasileiras de CS, rivalizando diretamente com a MIBR, que por muito tempo dominou o cenário nacional.",
        "A organização criou uma categoria de base para revelar novos talentos. Foi dessa iniciativa que surgiram jogadores como KSCERATO e ableJ, que ajudaram a equipe a crescer.",
        "O craque do futebol Neymar se envolveu com a organização, participando de eventos e interagindo com os jogadores. A FURIA também expandiu para outras modalidades, como FIFA, Valorant, Rainbow Six e Rocket League.",
    ]

    if "curiosidades" in mensagem or "fatos" in mensagem:
        estado_usuario[user_id] = "curiosidades"
        sort = random.choice(curiosidades)  
        await update.message.reply_text(f"{sort}\n\nQuer mais uma? Digita: mais uma.")

    # Escolhe outra curiosidade aleatória
    elif mensagem == "mais uma":
        if estado_usuario.get(user_id) == "curiosidades":
            sort = random.choice(curiosidades) 
            await update.message.reply_text(f"{sort}\n\nSe quiser outra, só digitar: mais uma.")
        else:
            await update.message.reply_text(f"Mais uma o quê? Me dá um contexto aí, {nome}!")



    elif "furia major" in mensagem or "major 2022" in mensagem or "furia rio" in mensagem:
        await update.message.reply_text(
        "No Major do Rio de 2022, a FURIA protagonizou um dos momentos mais emocionantes da história do CS:GO brasileiro. Eles venceram a poderosa NAVI, liderada por s1mple, diante de uma arena inteira torcendo enlouquecidamente. O Brasil parou pra assistir. Foi uma vitória histórica que consolidou a FURIA como símbolo nacional no CS!"
    )
        return

    
    elif "conquistas" in mensagem or "titulos" in mensagem:
        resposta = (
            "🏆 *Principais Conquistas da FURIA no CS* 🏆\n\n"
            "🥇 *DreamHack Masters Spring 2020 - América do Norte*\n"
            "🥇 *ESL Pro League Season 12 - América do Norte*\n"
            "🥇 *Intel Extreme Masters New York 2020 - América do Norte*\n"
            "🥇 *CBCS Elite League 2021 Season 1*\n"
            "🥇 *FiReLEAGUE Latin Power 2021*\n"
            "🥇 *BLAST Premier: Spring American Showdown 2023*\n"
            "🎖️ *Campeonatos regionais e classificações para Majors*\n\n"
            "🔥 A FURIA tem se consolidado como uma das melhores equipes brasileiras no cenário internacional!"
        )
        await update.message.reply_text(resposta, parse_mode="Markdown")
        return


    elif "tudo bem" in mensagem:
        respostas = [
            "Estava, acabei de cair de patente!😡",
            "Está sim! Subi uma patente hoje!😁😁",
            "Claro! Ainda mais com você aqui.🖤"
            ]
        
        resposta = random.choice(respostas)
        await update.message.reply_text(resposta)
        return
    
    elif "perdeu" in mensagem:
        await update.message.reply_text(f"Ganhar tudo também não tem graça, certo {nome}?")
        return

    elif "ganhou" in mensagem or "ganhando" in mensagem or "ganhar" in mensagem or "ganhamos" in mensagem:
        imagens = ["https://pbs.twimg.com/media/Ebd5UAaWAAAwvF3.png",
                   "https://pbs.twimg.com/media/FxUyy2DWwAAmRJd.jpg"]
        imagem = random.choice(imagens)
        await update.message.reply_photo(photo=imagem, caption="Foi fácil!")
        return
    
    #Memes em Gifs e texto

    elif "bang" in mensagem:
        gifs = ["https://media1.tenor.com/m/E8cSQd7OHcEAAAAC/flashbang-guy-screaming.gif", 
              "https://media1.tenor.com/m/CexnK1kDlNMAAAAd/flash-bang-csgo.gif", 
              "https://media.tenor.com/da8COCoZ7FgAAAAM/cat-funny-cat.gif"
        ]
        gif_url = random.choice(gifs)
        await update.message.reply_animation(animation=gif_url, caption="FLASHBANG!")
        return
    
    elif "animal favorito" in mensagem:
        respostas = [
        "Claro que é a nossa Pantera Negra! 🐾",
        "Sem dúvidas, a Pantera Negra. FURIA neles! 💥",
        "A Pantera Negra reina absoluta! 🏆",
        "É lógico que é a Pantera Negra! 🔥"
    ]
        resposta = random.choice(respostas)
        await update.message.reply_text(resposta)
        return

    
    elif "dance" in mensagem or "dançar" in mensagem:
        gifs = ["https://media1.tenor.com/m/E6ynXrh8lNoAAAAd/cs-go-dance.gif",
                "https://media1.tenor.com/m/A-xQ31GZ-RwAAAAd/cs-go.gif"]
        gif_url = random.choice(gifs)
        await update.message.reply_animation(animation=gif_url, caption="Toma essa!")
        return

    elif "granada" in mensagem:
        gif_url = "https://media1.tenor.com/m/R4zKVc1b-z0AAAAd/cs2-explosion.gif"
        await update.message.reply_animation(animation=gif_url, caption="Fire in the hole!")
        return
    
    elif "melhor sniper" in mensagem:
        gif_url = "https://media1.tenor.com/m/BOpnWn66KigAAAAd/hihi.gif"
        await update.message.reply_animation(animation=gif_url, caption="Óbvio que é o nosso FalleN")
        return
    
    #Condição para mensagem inválida ou não reconhecida

    else:
        resposta = [
        "Hmm, esse comando não encontrei no nosso arsenal! Digite /menu para ver tudo que posso fazer.",
        "Confuso como uma smoke mal jogada... Tente novamente usando /menu.",
        f"Não entendi o comando, {nome}! Chama o /menu pra ver as opções.",
    ]
    await update.message.reply_text(random.choice(resposta), parse_mode='Markdown')
    return

#Função de links úteis
async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    links = (
            "🔗 *Links Úteis da FURIA:*\n"
            "- [Liquipedia](https://liquipedia.net/counterstrike/FURIA)\n"
            "- [Twitter Oficial](https://twitter.com/FURIA)\n"
            "- [Site Oficial](https://www.furia.gg/)"
        )
    await update.message.reply_text(links, parse_mode="Markdown")

#Função de despedida do bot
async def sair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.from_user.first_name
    despedidas = [
        f"Fechando a call... Nos vemos nos servidores, {nome}",
        "Valeu pela visita! Partiu treinar aquela bang!",
        "Até logo, e boa sorte nos campos de batalha!"
        ]
    await update.message.reply_text(random.choice(despedidas))


#Inicialização do bot e configurações adicionais
if __name__ == "__main__":
    app = ApplicationBuilder().token("7388289738:AAFITBIkbisg4gfjsjl9dD3aeLUi0dsr7QY").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("historia", historia))
    app.add_handler(CommandHandler("links", links))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.add_handler(CommandHandler(["sair", "exit"], sair))
    print("Bot está rodando...")
    app.run_polling()
