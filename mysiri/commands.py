import subprocess
import re
from mysiri.get_answers import Fetcher


class Commander(object):
    def __init__(self):
        self.confirm = ["yes", "postive", "affirmative", "si", "do it", "yeah"]
        self.cancel = ["no", "cancel", "negative", "don't", "wait"]

    def discover(self, text: str):
        text = (text or "").lower().strip()

        if "what" in text and "name" in text:
            if "my name" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python commander. How are you?")
            return

        # Try to fetch an answer for arbitrary queries.
        query_text = re.sub(r"\s+", "+", text)
        print(f"Querying: {query_text}")
        f = Fetcher("https://www.google.com/search?q=" + query_text)
        answer = f.lookup()
        self.respond(answer)

        # Launch/open apps: only do this when the keywords are present.
        if "launch" in text or "open" in text:
            # Extract app name after the keyword and sanitize it
            app = text
            for kw in ("launch", "open"):
                if kw in text:
                    app = text.split(kw, 1)[1].strip()
                    break

            # Keep only safe characters for an app name (letters, digits, space, - , _)
            app = re.sub(r"[^A-Za-z0-9 _-]", "", app).strip()
            if not app:
                self.respond("I couldn't determine which app to open.")
                return

            # Use subprocess with argument list to avoid shell injection
            try:
                subprocess.run(["open", "-a", f"{app}.app"], check=False)
                self.respond(f"Attempting to open {app}")
            except FileNotFoundError:
                self.respond("The open command is not available on this system.")
            except Exception as exc:
                self.respond(f"Failed to open {app}: {exc}")

        if "fine thank you" in text:
            self.respond("Shall I move to another task")

    def respond(self, response: str):
        print(response)
        # Use subprocess without shell=True to avoid shell quoting issues.
        try:
            subprocess.call(["say", response])
        except Exception:
            # If TTS isn't available, just print the response (silently ignore TTS errors)
            pass
