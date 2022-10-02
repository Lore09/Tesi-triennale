#!/bin/bash

if [ ! -d venv ]
then
pip install virtualenv
virtualenv venv
fi

source venv/bin/activate
pip install -r requirements.txt
python3 main.py
