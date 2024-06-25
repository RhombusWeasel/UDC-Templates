#!/bin/bash

set -e

python3 -m venv .json_env
source .json_env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 app.py