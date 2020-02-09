#!/bin/sh


# Usage: echo "Enter Project name"
project=$1 
echo $project
mkdir $project && cd $project/
touch .gitignore
echo "__pycache__" >> .gitignore
touch config.py
touch run.py
touch requirements.txt
ls -lah
mkdir app && cd app
touch __init__.py
touch models.py
touch views.py

mkdir templates
touch templates/index.html
cd ..
ls -lah
echo "Done ......."
