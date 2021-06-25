from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "/Users/shubham/Development/chromedriver"
SCROLL_PAUSE_TIME = 0.5
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

class InstaFollower:
    def __init__(self, name):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.people = []
        self.search_key = name

    def login(self):
        self.driver.get(URL)

        time.sleep(3)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)

    def find_followers(self):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(self.search_key)
        time.sleep(3)
        account_name = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        account_name.click()
        # search.send_keys(Keys.ENTER)
        time.sleep(1)
        # search.send_keys(Keys.ENTER)

        time.sleep(4)

        followers = self.driver.find_element_by_css_selector("ul li a")
        followers.click()

        time.sleep(1)

        for i in range(10):
            person = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", person)
            time.sleep(2)

    def follow(self):
        self.people = self.driver.find_elements_by_css_selector("li button")
        for person in self.people:
            person.click()
            time.sleep(1)

        # self.driver.quit()

