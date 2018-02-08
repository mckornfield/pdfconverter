### Setup

Prereq: Python3

First you will need to create an api_key.txt file, which contains a key (no quotes). You can get them from here: https://pdftables.com/pdf-to-excel-api

Second you will need to load the virtual environment using `source venv/Scripts/activate`

Third you will need to install the pdf client `pip install git+https://github.com/pdftables/python-pdftables-api.git` (actually this should already be done by loading the virtualenv)

### Usage

The script takes one argument, -f or --folder, which is the path to the folder of pdfs to convert

The API key is rate limited to 50 by default. It is 15 dollars for 500 pages worth of conversion (which is fairly decent)
Currently coded, an api_key.txt file must be in the same folder as the script or executable or the script will not work

You can type `python convert.py -h` to see how to use it

## Installer

An executable can be generated using `pyinstaller convert.spec`pip install git+https://github.com/pdftables/python-pdftables-api.git. It will generate an executable and a folder inside a /dist folder
