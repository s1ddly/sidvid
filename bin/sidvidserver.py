#!/usr/bin/env python3
from pytubefix import YouTube
import os
import discord
from discord import File
import time
from datetime import datetime
import subprocess

token = open("token","r").read()
igname = open("iguname","r").read()
igpwd = open("igpwd","r").read()

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
                if "youtu" in message.content.lower():
                    if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                        if yt_getsize(invid) < 26214400:
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
                        if tiktoksize < 26214400:
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
                        fbsize = "26214400"
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
                        if twittersize < 26214400:
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
                elif "instagram" in message.content.lower():
                    instatime = str(int(time.time_ns()))
                    instatype = message.content.split("/")[3]
                    instaid = message.content.split("/")[4]
                    instapath = "output/" + instatime
                    instadesc = ""
                    instaflist = []
                    
                    print(str(datetime.now()) + " Instagram: " + instatype + ":" + instaid)
                    
                    if instatype == "p" or instatype == "reel":
                        instadl = subprocess.run(["instaloader", "--dirname-pattern", instapath, "--login=" + igname, "--password=" + igpwd, "--no-video-thumbnails", "--", "-" + instaid])
                    elif instatype == "stories":
                        instadl = subprocess.run(["instaloader", "--dirname-pattern", instapath, "--login=" + igname, "--password=" + igpwd, instaid, "--stories", "--no-posts", "--no-profile-pic", "--no-video-thumbnails"])
                    
                    for filename in os.listdir(instapath):
                        fname = os.path.join(instapath, filename)
                        if fname[-4:] == ".txt":
                            instadesc = open(fname, "r").read()
                            
                        if instatype == "reel":
                            if fname[-4:] == ".mp4":
                                instasize = os.stat(fname).st_size
                                if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                                    if instasize < 26214400:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 2:
                                    if instasize < 52428800:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 3:
                                    if instasize < 104857600:
                                        instaflist.append(discord.File(fname))
                        elif instatype == "p":
                            if fname[-4:] == ".mp4" or fname[-4:] == ".jpg" or fname[-4:] == ".png":
                                instasize = os.stat(fname).st_size
                                if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                                    if instasize < 26214400:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 2:
                                    if instasize < 52428800:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 3:
                                    if instasize < 104857600:
                                        instaflist.append(discord.File(fname))
                        elif instatype == "stories":
                            if fname[-4:] == ".mp4" or fname[-4:] == ".jpg" or fname[-4:] == ".png":
                                instasize = os.stat(fname).st_size
                                if message.guild.premium_tier == 0 or message.guild.premium_tier == 1:
                                    if instasize < 26214400:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 2:
                                    if instasize < 52428800:
                                        instaflist.append(discord.File(fname))
                                elif message.guild.premium_tier == 3:
                                    if instasize < 104857600:
                                        instaflist.append(discord.File(fname))
                                        
                    if len(instaflist) == 0:
                        raise Exception("Error in Insta DL")
                    else:
                        await message.channel.send(message.author.mention + ": " + instadesc, files=instaflist)
            except:
                await message.channel.send(message.author.mention + " There was an error with the download :o, please check the message and try again")
client.run(token)
