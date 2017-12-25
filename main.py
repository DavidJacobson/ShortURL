## David Jacobson

import argparse
import validators.url
import os
import requests
import platform

parser = argparse.ArgumentParser(description="Shorten a URL.")
parser.add_argument('url', metavar='U', help='URL to be shortened')
parser.add_argument('--apikey', metavar='A', help="Your API Key, if it hasn't already been set", default=None)
args = parser.parse_args()

def main():
    # First, ensure the URL is valid
    if not validators.url(args.url):
        print("Please enter a valid URL.")
        exit(1)
    # Next, let's ensure there is an API key (If the key is invalid, the program will fail later)
    if os.getenv("short_apikey", "None") == "None": # If the key has never been set
        if args.apikey == None: # And the user has not set the key this time
            print("Please add your API key (This does not need to be done in the future)")
            exit(1)
        else: # Set the API key
            # Ensure cross-compatability
            if platform.system() == "Windows": # Windows ENV variables need to be set this way...
                os.system("setx short_apikey {}".format(args.apikey))
            elif platform.system() == "Linux":
                os.system("export short_apikey=\"{}\"".format(args.apikey))
            else:
                print("The system you are running is not supported.")
                exit(1)
    # Now, request the shortened URL
    request = requests.post("http://tiny-url.info/api/v1/create",
                            {"format": "json",
                             "apikey":args.apikey,  # Note - using this and not env because the variable may not update
                             "provider":"bit_ly",
                             "url":args.url})
    response = request.json()
    if response["state"] == "error":
        print("An error was encountered. Please verify your key.")
        exit(1)
    print(response["shorturl"])

if __name__ == '__main__':
    main()


