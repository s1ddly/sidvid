#!/usr/bin/env bash
echo "Starting server!"
echo "Setting up Virtual Environment"
pip install virtualenv
python3 -m virtualenv sidvidpy
source sidvidpy/bin/activate
echo "Installing the required libraries in the venv"
pip install pytube
pip install discord.py
echo "Executing python"
python3 sidvidserver.py
echo "Shutting down venv "
deactivate
echo "Successfully shut down the server!"