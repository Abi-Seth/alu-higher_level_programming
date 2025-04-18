#!/usr/bin/python3
""" Sends a POST request with an email to a specified URL. """
import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=email)
    print(r.text)
