import discord
from discord.ext import commands
from bot_logic import gen_pass
from emoji_logic import gen_emodji

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}")

@bot.command()
async def pasw(ctx, numero):
    numer = int(numero)
    await ctx.send(gen_pass(numer))

@bot.command()
async def emoji(ctx):
    emoji = gen_emodji()
    await ctx.send(f"Aquí tienes un emoji aleatorio: {emoji}")

bot.run("")   
