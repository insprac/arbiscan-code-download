#!/bin/python3

import argparse
import requests
import re
import os
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
    description="Download contract code from arbiscan.io"
)
parser.add_argument(
    "address",
    help="Arbitrum contract address"
)
parser.add_argument(
    "--out",
    dest="out",
    required=True,
    help="Output directory"
)

args = parser.parse_args()

url = "https://arbiscan.io/address/%s#code" % args.address
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "html.parser")

code_wrapper_div = soup.find("div", {"id": "dividcode"})

if code_wrapper_div == None:
    raise Exception(
        "Couldn't find the code wrapper div, please ensure the contract " +
        "exists and the code has been provided: %s" % url
    )

headings = code_wrapper_div.find_all(text=re.compile("^File \d+ of \d+ : "))
code_editors = code_wrapper_div.find_all("pre", "editor")

if len(headings) != len(code_editors):
    raise Exception(
        "The number of headings (%d) doesn't match editors (%d)" % (
            len(headings),
            len(code_editors)
        )
    )

if len(headings) == 0:
    raise Exception(
        "No code was found, please ensure the code for the contract was " +
        "provided: %s" % url
    )

for i in range(len(headings)):
    filename = headings[i].split(":", 1)[1].strip()
    code = code_editors[i].text
    path = os.path.join(args.out, filename)

    print("Writing %s" % path)

    f = open(path, "w")
    f.write(code)
    f.close()
