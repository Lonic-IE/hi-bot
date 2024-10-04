import discord
from discord.ext import commands
from discord.ui import Button, View
from services.new_channel import WelcomeView
# Substitua com o ID do seu servidor e o token do bot
id_servidor = 1237392372925726823  # Substitua pelo ID do seu servidor
id_canal = 1291788110497321051

# Leia o token do arquivo
with open('token.env', "r") as token_file:
    api = token_file.readline().strip()

# Configuração dos Intents
intents = discord.Intents.default()
intents.message_content = True  # Permissão para acessar o conteúdo das mensagens
intents.guilds = True
intents.guild_messages = True

# Criação do bot com prefixo de comando e Intents
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    
    # Sincronizar comandos de barra (slash commands) com um servidor específico
    guild = discord.Object(id=id_servidor)
    await bot.tree.sync(guild=guild)
    print('Comandos de barra sincronizados com o servidor.')

    # Pegar id do canal
    channel = bot.get_channel(id_canal)
    if channel:
        message_exits = channel.history(limit=1)
        if message_exits:
            print(message_exits)

    # Enviar mensagem de boas-vindas ao canal especificado com o botão

            message_standard = (
                "🌟 **Bem-vindo ao serviço da XX!** 🌟\n\n"
                "Estamos aqui para ajudar você a alcançar o rank dos seus sonhos! 🚀 "
                "text "
                "text!\n\n"
                "**Entre em contato e comece sua jornada para o sucesso!** 🎮✨\n\n"
                "Desenvolvimento do bot © Lonic IE. Todos os direitos reservados.\n\n"
                "Para mais informações, acesse: https://github.com/Lonic-IE."
            )
            view = WelcomeView()  # Criação da view com o botão
            await channel.send(message_standard, view=view)
        else:
            print(f'Canal {id_canal} não encontrado.')

@bot.command(name="sobre")
async def message_sobre(ctx):
    hi_bot_description = (
        "Hi-Bot é o seu assistente no Discord para a comercialização de serviços. "
        "Ele facilita agendamentos, gerencia pagamentos e conecta clientes e prestadores de serviços de forma rápida e eficiente."
    )
    await ctx.send(hi_bot_description)
# Executar o bot
bot.run(api)
