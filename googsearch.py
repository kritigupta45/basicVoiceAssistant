from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class gosearch():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/kriti/driver/chromedriver_win32/chromedriver.exe'))

    def inf(self, query):
        self.query = query
        self.driver.get(url="https://www.google.com")
        search = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        enter.click()