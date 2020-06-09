import subprocess
import os
import requests
import re
from bs4 import BeautifulSoup
from get_answers import Fetcher


class Commander(object):
    def __init__(self):
        self.confirm = ["yes", "postive", "affirmative", "si", "do it", "yeah"]
        self.cancel = ["no", "cancel", "negative", "don't", "wait"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my name" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python commander. How are you?")
        else:
            text = re.sub(" ", "+", text)
            print(text)
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            os.system("open -a " + app + ".app")

        # if "close" in text:
        #     app = text.split(" ", 1)[-1]
        #     os.system("osascript -e 'quit app {0}".format(app))

        # if "quit" in text:
        #     self.respond("Are you sure you want to exit?")
        #     if "yes" in text:
        #         self.respond("See your later alligator!")

        if "fine thank you" in text:
            self.respond("Shall I move to another task")

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)
