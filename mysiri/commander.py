import subprocess


class Commander(object):
    def __init__(self):
        self.confirm = ["yes", "postive", "affirmative", "si", "do it"]
        self.cancel = ["no", "cancel", "negative", "don't", "wait"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python commander. How are you?")

        if "quit" in text:
            self.respond("Are you sure you want to exit?")
            if "yes" in text:
                self.respond("See your later alligator!")

        if "fine thank you" in text:
            self.respond("Shall I move to another task")

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)
