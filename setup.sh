#!/usr/bin/env bash
echo "Starting server!"
echo "Setting up Virtual Environment"
pip install virtualenv==20.16.2
python3 -m virtualenv sidvidpy
source sidvidpy/bin/activate
echo "Installing the required libraries in the venv"
pip install pytube==12.1.0
pip install discord.py==1.7.3
pip install selenium==4.4.3
echo "Executing python"
python3 -u bin/sidvidserver.py
echo "Shutting down venv "
deactivate
echo "Successfully shut down the server!"