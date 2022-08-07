#!/usr/bin/env bash
pip install virtualenv
python3 -m virtualenv sidvidpy
source sidvidpy/bin/activate
pip install pytube
python3 sidvidserver.py
deactivate