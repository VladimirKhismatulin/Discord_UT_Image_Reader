import discord
import random
import os
from model import get_class
from discord.ext import commands
from discord import Attachment

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я бот этого сервера!')
    await ctx.send("Пришли картинку с командой /image и я попробую угадать персонажа.")


@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) != 0:
        for attachment in ctx.message.attachments:
            await attachment.save(f"images\{attachment.filename}")
            sans = get_class(f"images\{attachment.filename}")
            if sans == "Ut! Sans":
                await ctx.send("Я думаю, это Undertale Санс.")
                await ctx.send("Классический санс - самый известный из всех.")
            elif sans == "Us! Papyrus":
                await ctx.send("Я думаю, это Underswap Папирус.")
                await ctx.send("Играет роль Санса в параллельной вселенной.")
            elif sans == "Uf! Sans":
                await ctx.send("Я думаю, это Underfell Санс.")
                await ctx.send("Озлобленный Санс, живущий в озлобленном мире.")
            elif sans == "Ot! Sans":
                await ctx.send("Я думаю, это Outertale Санс.")
                await ctx.send("Санс, живущий в просторах космоса.")
            await ctx.send("Если я ошибся, возможно я не знаю такого персонажа.")
            await ctx.send("Чтобы посмотреть список персонажей, введи /list.")
    else:
        await ctx.send("Файл не найден.")


#@bot.command()
#async def help(ctx):
    #await ctx.send("!Help - показывает команды (как ты и догадался), !hint - даёт совет об экологии, !mem - скидывает мем про экологию, !hello - приветствуется с вами.")

bot.run("TOKEN")
