import requests
from bs4 import BeautifulSoup


class Fetcher(object):
    """Simple fetcher that retrieves a reasonable textual answer for a URL.

    This implementation uses requests + BeautifulSoup and returns, in order of
    preference:
      - the page meta description
      - the page <title>
      - a short snippet from the page text

    It's intentionally defensive and will return a short "I don't know"
    message on error instead of raising.
    """

    def __init__(self, url: str):
        self.url = url

    def lookup(self) -> str:
        headers = {"User-Agent": "mysiri/0.1 (+https://example.local)"}

        try:
            resp = requests.get(self.url, headers=headers, timeout=8)
        except Exception as exc:
            print(f"Fetcher: request failed: {exc}")
            return "I don't know"

        if resp.status_code != 200:
            print(f"Fetcher: non-200 status {resp.status_code}")
            return "I don't know"

        soup = BeautifulSoup(resp.text, "html.parser")

        # Prefer a meta description if present
        meta = soup.find("meta", attrs={"name": "description"})
        if meta and meta.get("content"):
            return meta["content"].strip()

        # Fallback to title
        if soup.title and soup.title.string:
            return soup.title.string.strip()

        # As a last resort, return a short snippet of text
        text = soup.get_text(separator=" ").strip()
        if not text:
            return "I don't know"

        snippet = " ".join(text.split())[:300]
        return snippet + ("..." if len(text) > 300 else "")
