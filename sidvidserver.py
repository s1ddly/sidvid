#!/usr/bin/env python3
from pytube import YouTube
import os
import discord
from discord import File
import time
from datetime import datetime

token = open("token","r").read()

client = discord.Client()

def yt_dl(inlink, fname):
    yt = YouTube(inlink)
    print(str(datetime.now()) + " " + yt.title)
    print(str(datetime.now()) + " Filesize: " + str(yt.streams.filter(progressive=True).order_by('resolution').desc().first().filesize))
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path="./output", filename=fname)
    return("output/" + fname)
    
def yt_getsize(inlink):
    yt = YouTube(inlink)
    return(yt.streams.filter(progressive=True).order_by('resolution').desc().first().filesize)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if message.content[0:4] == "-dl ":
            invid = message.content.split(" ")[1]
            print(str(datetime.now()) + " " + message.author.name + ", " + message.guild.name + " Tried to download: " + invid)
            try:
                if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                    if yt_getsize(invid) < 8388608:
                        await message.channel.send(message.author.mention, file=File(yt_dl(message.content,str(int(time.time_ns())) + ".mp4")))
                    else:
                        await message.channel.send(message.author.mention + " Failed to download, file is over 8mb(" + str(yt_getsize(invid)) + " bytes) :(")
                elif message.guild.premium_tier == 2:
                    if yt_getsize(invid) < 52428800:
                        await message.channel.send(message.author.mention, file=File(yt_dl(message.content,str(int(time.time_ns())) + ".mp4")))
                    else:
                        await message.channel.send(message.author.mention + " Failed to download, file is over 50mb(" + str(yt_getsize(invid)) + " bytes) :(")
                elif message.guild.premium_tier == 3:
                    if yt_getsize(invid) < 104857600:
                        await message.channel.send(message.author.mention, file=File(yt_dl(message.content,str(int(time.time_ns())) + ".mp4")))
                    else:
                        await message.channel.send(message.author.mention + " Failed to download, file is over 100mb(" + str(yt_getsize(invid)) + " bytes) :(")
            except:
                await message.channel.send(message.author.mention + " There was an error with the download :o, please check the message and try again")
client.run(token)
