#!/usr/bin/env python3
from pytube import YouTube
import os
import discord
from discord import File
import time
from datetime import datetime
import subprocess

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
    elif(message.author.id == 1015483649946304593):
        await message.channel.send("CUM", reference=message)
    else:
        if message.content[0:4] == "-dl ":
            invid = message.content.split(" ")[1]
            print(str(datetime.now()) + " " + message.author.name + ", " + message.guild.name + " Tried to download: " + invid)
            try:
                if "youtu" in message.content.lower():
                    if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                        if yt_getsize(invid) < 8388608:
                            await message.channel.send(message.author.mention, file=File(yt_dl(invid,str(int(time.time_ns())) + ".mp4")))
                        else:
                            await message.channel.send(message.author.mention + " Failed to download, file is over 8mb(" + str(yt_getsize(invid)) + " bytes) :(")
                    elif message.guild.premium_tier == 2:
                        if yt_getsize(invid) < 52428800:
                            await message.channel.send(message.author.mention, file=File(yt_dl(invid,str(int(time.time_ns())) + ".mp4")))
                        else:
                            await message.channel.send(message.author.mention + " Failed to download, file is over 50mb(" + str(yt_getsize(invid)) + " bytes) :(")
                    elif message.guild.premium_tier == 3:
                        if yt_getsize(invid) < 104857600:
                            await message.channel.send(message.author.mention, file=File(yt_dl(invid,str(int(time.time_ns())) + ".mp4")))
                        else:
                            await message.channel.send(message.author.mention + " Failed to download, file is over 100mb(" + str(yt_getsize(invid)) + " bytes) :(")
                elif "tiktok" in message.content.lower():
                    tiktokinfo = subprocess.run(["you-get", "-i", invid], capture_output=True)
                    tiktoksize = int(str(tiktokinfo.stdout).split("Size")[1].split("(")[1].split(")")[0].split(" Bytes")[0])
                    tiktoktitle = str(str(tiktokinfo.stdout).split("\\n")[1].split("      ")[1])
                    print(str(datetime.now()) + " " + tiktoktitle)
                    print(str(datetime.now()) + " Filesize: " + str(tiktoksize))
                    tiktoktime = str(int(time.time_ns()))
                    if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                        if tiktoksize < 8388608:
                            tiktokdl = subprocess.run(["you-get", "-o", "output", "-O", tiktoktime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + tiktoktime + ".mp4"))
                    elif message.guild.premium_tier == 2:
                        if tiktoksize < 52428800:
                            tiktokdl = subprocess.run(["you-get", "-o", "output", "-O", tiktoktime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + tiktoktime + ".mp4"))
                    elif message.guild.premium_tier == 3:
                        if tiktoksize < 104857600:
                            tiktokdl = subprocess.run(["you-get", "-o", "output", "-O", tiktoktime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + tiktoktime + ".mp4"))
                elif "facebook" in message.content.lower() or "fb.watch" in message.content.lower():
                    fbtime = str(int(time.time_ns()))
                    fbname = fbtime + ".mp4"
                    fbsize = ""
                    if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                        fbsize = "8388608"
                    elif message.guild.premium_tier == 2:
                        fbsize = "52428800"
                    elif message.guild.premium_tier == 3:
                        fbsize = "104857600"
                    print(str(datetime.now()) + " " + invid)
                    print(str(datetime.now()) + " Filesize: Unknown")
                    fbdl = subprocess.run(["youtube-dl", "--max-filesize", fbsize, invid, "-o", "output/" + fbname, "-f", "mp4"])
                    if fbdl.returncode == 0:
                        await message.channel.send(message.author.mention, file=File("output/" + fbname))
                    else:
                        raise Exception("Error in fb DL")
                elif "twitter" in message.content.lower():
                    twitterinfo = subprocess.run(["you-get", "-i", invid], capture_output=True)
                    twittersize = int(str(twitterinfo.stdout).split("Size")[1].split("(")[1].split(")")[0].split(" Bytes")[0])
                    twittertitle = str(str(twitterinfo.stdout).split("\\n")[1].split("      ")[1])
                    print(str(datetime.now()) + " " + twittertitle)
                    print(str(datetime.now()) + " Filesize: " + str(twittersize))
                    twittertime = str(int(time.time_ns()))
                    if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                        if twittersize < 8388608:
                            twitterdl = subprocess.run(["you-get", "-o", "output", "-O", twittertime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + twittertime + ".mp4"))
                    elif message.guild.premium_tier == 2:
                        if twittersize < 52428800:
                            twitterdl = subprocess.run(["you-get", "-o", "output", "-O", twittertime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + twittertime + ".mp4"))
                    elif message.guild.premium_tier == 3:
                        if twittersize < 104857600:
                            twitterdl = subprocess.run(["you-get", "-o", "output", "-O", twittertime, invid])
                            await message.channel.send(message.author.mention, file=File("output/" + twittertime + ".mp4"))
            except:
                await message.channel.send(message.author.mention + " There was an error with the download :o, please check the message and try again")
client.run(token)
