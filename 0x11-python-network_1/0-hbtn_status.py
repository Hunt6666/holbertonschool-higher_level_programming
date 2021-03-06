#!/usr/bin/python3
""" prints body response """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
    html = r.read()
    print("Body response:")
    print("\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + str(html.decode('utf-8')))
