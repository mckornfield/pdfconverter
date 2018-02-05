import sys
import pdftables_api
import argparse
import glob
import os

#Parse arguments
parser = argparse.ArgumentParser(description='Creates an xlsx spreadsheet from a pdf file')
parser.add_argument('-f','--folder', help='Path to Folder', required=True)
args = parser.parse_args()

#Read API Key
with open('api_key.txt') as key_file:
    for line in key_file:
        key = line.strip()
if not key:
    raise Exception("You must specify an API key within an api_key.txt file in this same directory")


print("Key is " + key)
sys.stdout.flush()

# Get filename

client = pdftables_api.Client(key)
files = glob.glob("{}/*.pdf".format(args.folder))
print(files)
for pdfName in files:
    xlsxName = os.path.splitext(pdfName)[0] + ".xlsx"
    print("Attempting to create file: " + xlsxName + " from " + pdfName)
    sys.stdout.flush()
    client.xlsx_single(pdfName, xlsxName)
    print("File created successfully")
    sys.stdout.flush()
