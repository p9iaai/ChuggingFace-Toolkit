#!/bin/bash

echo "Setting up the environment..."

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo "Creating folder structure..."

echo "Creating .logs..."
if [ ! -d ".logs" ]; then
  mkdir .logs
fi

echo "Creating input folders..."
if [ ! -d "input" ]; then
  mkdir input
fi

echo "Creating output folders..."
if [ ! -d "output" ]; then
  mkdir output
fi

echo "Folder structure created successfully."

if [ ! -f ".env" ]; then
  touch .env
  echo "Created empty .env file..."
fi

echo "Environment setup complete."

echo "Ready!"

echo "Don't forget to add your 🤗HuggingFace token to the .env file"

echo "Now you can run the tools in the tools folder."
