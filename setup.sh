#!/usr/bin/env bash
echo "Starting server!"
echo "Setting up Virtual Environment"
pip install virtualenv==20.16.2
python3 -m virtualenv sidvidpy
source sidvidpy/bin/activate
echo "Installing the required libraries in the venv"
pip install pytube==15.0.0
pip install discord.py==1.7.3
pip install you-get==0.4.1620
pip install youtube-dl==2021.12.17
pip install instaloader==4.13.1
echo "Executing python"
python3 -u bin/sidvidserver.py
echo "Shutting down venv "
deactivate
echo "Successfully shut down the server!"