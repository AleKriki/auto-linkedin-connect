from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # abre navegador em tela cheia
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def open(self, url: str):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()