import os
import string
import discord
from dotenv import load_dotenv
from discord.ext import commands

from cipher_handling import encrypt_text, decrypt_text

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def make_key(symbols):
    key = {}
    for index, letter in enumerate(string.ascii_uppercase):
        key[letter] = symbols[index].lower()
    print (key)
    return key



KEY = make_key(os.getenv("KEY"))


bot = commands.Bot(command_prefix="!")





@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="encrypt", help="Encrypts the message typed. Must be in quotes")
async def encrypt(ctx, message):
    text = encrypt_text(message, KEY.copy())
    await ctx.send(text)

@bot.command(name="decrypt", help="Decrypts the message typed using this bot's key. Must be in quotes")
async def decrypt(ctx, message):
    text = decrypt_text(message, KEY.copy())
    
    await ctx.send(text)



bot.run(TOKEN)