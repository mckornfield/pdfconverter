### Setup

Prereq: Python3, pip

1. Make sure python3 is installed using `python --version`
1. Load a virtual environment in this directory if it's the first time, using `python -m venv venv`
1. Source the virtual enviroment (this will need to be done every time you open a new terminal)
```
source venv/Scripts/activate
```
1. Make sure pip is installed using `pip --version`
1. Run `pip install -r requirements.txt`

NOTE: You will need to source the virtual environment after first time setup but everything else is only required if the `venv` directory is deleted

### Usage

The script takes one argument, -f or --folder, which is the path to the folder of pdfs to convert

The API key is rate limited to 50 by default. It is 15 dollars for 500 pages worth of conversion (which is fairly decent)
Currently coded, an api_key.txt file must be in the same folder as the script or executable or the script will not work

You can type `python convert.py -h` to see how to use it

### Installer

An executable can be generated using `pyinstaller convert.spec`. It will generate an executable and a folder inside a /dist folder. Simply move the api_key.txt document into the same folder and it will run automatically on any `pdfs` folder. Can also be run with a path argument via the cmd prompt.
