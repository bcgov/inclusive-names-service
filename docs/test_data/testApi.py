#! /usr/local/bin/python3

# imports
import argparse
import requests
import csv
import json

# Example call python3 testApi.py -u https://my-api.com/api/data/create --method POST --useField name --csv ir_bands.csv --additionalData '{"field1": "value1", "field2": "value2"}'
parser = argparse.ArgumentParser(description='UTF8 API Tester with csv files')
parser.add_argument('-u', '--url', help='The endpoint of the API', required=True)
parser.add_argument('-m', '--method', help='The request method to use (GET/POST/PUT/DELETE/HEAD etc)', required=True)
parser.add_argument('-f', '--useField', help='The field to put the csv data in', required=True)
parser.add_argument('-c', '--csv', help='The csv to read from', required=True)
parser.add_argument('-d', '--additionalData', help='Other required(or desired) data to make the call', required=False)
parser.add_argument('-j', '--jwt', help='Optional JWT Token for authentication header', required=False)

# Parse the command-line arguments
args = parser.parse_args()

# get the base params
params = {}
if args.additionalData:
  params = json.loads(args.additionalData)

headers = {}
if args.jwt:
  headers={
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(args.jwt)
  }

print("Opening file: " + args.csv + " for " + args.method + " url: " + args.url)
# build a request using the arguments
with open(args.csv, 'r', newline='') as f:
  method = getattr(requests, args.method.lower())

  reader = csv.reader(f)

  # assume header row
  skipped = False
  for row in reader:
      if skipped:
        # Process each row
        for value in row:
          params[args.useField] = value
          response = method(args.url, json=params, headers=headers)
          try:
            print("Response for " + value + " is\n" + response.json())
          except:
            print("Response for " + value + " is\n" + response.text)
      skipped = True