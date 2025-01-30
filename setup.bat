@echo off
echo Setting up the environment...

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo Creating folder structure...

echo Creating .folders...
if not exist .logs mkdir .logs

echo Creating input folders...
if not exist input mkdir input

echo Creating output folders...
if not exist output mkdir output

echo Folder structure created successfully.

if not exist .env echo. > .env

echo Created empty .env file...

echo Environment setup complete.

echo Ready!

echo Don't forget to add your 🤗HuggingFace token to the .env file

echo Now you can run the tools in the tools folder.