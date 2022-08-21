from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/kriti/driver/chromedriver_win32/chromedriver.exe'))

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()


