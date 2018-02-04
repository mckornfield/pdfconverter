import pdftables_api
import argparse

#Parse arguments
parser = argparse.ArgumentParser(description='Creates an xlsx spreadsheet from a pdf file')
parser.add_argument('-p','--pdf', help='Path to PDF', required=True)
parser.add_argument('--name', help='Name of created file')
args = parser.parse_args()

#Read API Key
with open('api_key.txt') as key_file:
    for line in key_file:
        key = line.strip()
if not key:
    raise Exception("You must specify an API key within an api_key.txt file in this same directory")

print("Key is " + key)

# Get filename
file_name = args.name if args.name is not None else 'output'
print("Filename = " + file_name) 
print("Attempting to create file: " + file_name + ".xlsx from " + args.pdf)

client = pdftables_api.Client(key)
client.xlsx(args.pdf, file_name)

print("File created successfully")
