#!/usr/bin/env python3
from pytube import YouTube
import os
import discord




def yt_test():
    yt = YouTube('https://www.youtube.com/watch?v=x7X9w_GIm1s')
    print(yt.title)
    print("Filesize: " + str(yt.streams.filter(progressive=True).order_by('resolution').desc().first().filesize))
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path="./output")