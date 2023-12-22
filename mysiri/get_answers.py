from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup


class Fetcher(object):
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)
        self.lookup()

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "gsfi"))
            )
            print(ip, " found.   Continue processing...")
        except Exception as e:
            print(f"Failed to get page. {e}")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="_sPg")
        print(type(answer))
        print("=" * 18)
        print(dir(answer))
        print("=" * 18)

        if not answer:
            answer = soup.findAll(class_="_XMK")

        if not answer:
            answer = "I don't know"

        self.driver.quit()
        return answer.get_text()
