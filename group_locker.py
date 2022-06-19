import discord
import requests
import os
import ctypes
import json
from discord.ext import commands

ctypes.windll.kernel32.SetConsoleTitleW(f"Group Locker - Made By Astraa")
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = config.get('prefix')

def getheaders(token):
    headers = {"Content-Type": "application/json", "Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0"}
    return headers

def Init():
    token = config.get('token')
    prefix = config.get('prefix')
    if token == "":
        os.system("cls")
        input(f"Please set a token in the config.json file.")
        return
    elif prefix == "":
        os.system("cls")
        input(f"Please set a prefix in the config.json file.")
        return
    try:
        Astraa.run(token, bot=False, reconnect=True)
    except:
        os.system("cls")
        input(f"The token located in the config.json file is invalid")
        return

Astraa = discord.Client()
Astraa = commands.Bot(description='ATIO Tool - SelfBot created by Astraa', command_prefix=prefix, self_bot=True)
Astraa.Locker = False

@Astraa.event
async def on_ready():
    os.system("cls")
    print(f"Logged in as {Astraa.user.name} - Prefix: {prefix}\nType {prefix}lock to see the commands\n")

@Astraa.event
async def on_message(message):
    if Astraa.Locker == True:
        #Lock Joins
        #No idea... If you have one, create an issue on github

        #Lock Leaves
        if message.content == "":
            try:
                res = requests.put(f"https://discord.com/api/v8/channels/{message.channel.id}/recipients/{message.author.id}", headers={"authorization":token})
            except Exception as e:
                print(e)
                pass
    await Astraa.process_commands(message)

@Astraa.command(aliases=["locker", "locked", "grouplocker", "lockgroup"])
async def lock(ctx, value=None):
    if value == "ON" or value == "on":
        Astraa.Locker = True
        await ctx.message.edit(content=f"Groupchat is now **locked**!", delete_after=5)
    elif value == "OFF" or value == "off":
        Astraa.Locker = False
        await ctx.message.edit(content=f"Groupchat is now **unlocked**!", delete_after=5)
    else:
        await ctx.message.edit(content=f'[ERROR]: Invalid input! Command: `*lock <ON/OFF>`', delete_after=5)
        return

if __name__ == '__main__':
    Init()