#!/usr/bin/python3
"""
    Fetch data from alx intranet
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {format(type(body))}")
        print(f"\t- content: {format(body)}")
        print(f"\t- utf8 content: {format(body.decode("utf-8"))}")
