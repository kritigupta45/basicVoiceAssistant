from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/kriti/driver/chromedriver_win32/chromedriver.exe'))

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+ query)
        video = self.driver.find_element("xpath", '//*[@id="dismissable"]')
        video.click()

