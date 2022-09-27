#!/usr/bin/python3

"""
This is script dumps all arguments to a json file
All command line arguments are stored in a json
file add_item.json
"""


import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__(
        "6-load_from_json_file"
    ).load_from_json_file


filename = "add_item.json"
e_args = []

args = sys.argv[1:]

if os.path.exists(filename):
    data = load_from_json_file(filename)

    if isinstance(data, list):
        e_args = data

e_args.extend(args)

save_to_json_file(e_args, filename)
