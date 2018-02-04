### Setup

Prereq: Python3

First you will need to create an api_key.txt file, which contains a key (no quotes). You can get them from here: https://pdftables.com/pdf-to-excel-api

Second you will need to load the virtual environment using `source venv/Scripts/activate`

Third you will need to install the pdf client `pip install git+https://github.com/pdftables/python-pdftables-api.git`

### Usage

The script takes two arguments, --pdf or -p as the path to the pdf file, and --name or -n as the name of the output xslx file

You can type `python convert.py -h` to see how to use it
