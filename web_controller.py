from chatbot import Chatbot
from util.message import Message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import time
from util.XPATHS import *

my_group = "threadId"


# TODO use only xpaths!


class WebController:
    timeout = 10

    def __init__(self, chatbot=Chatbot("username", "password", 3644096069038782)):
        self.chatbot = chatbot
        self.driver = webdriver.Chrome("chromedriver.exe")
        self._message_wait = WebDriverWait(self.driver, self.chatbot.refresh_rate)
        self._wait = WebDriverWait(self.driver, 5)
        self._time = time()
        print("init starts")
        # init driver todo: do it somewhere else
        print(f"Pybot: Initializing driver...\nDriver: {self.driver}")
        self.driver.get(f"https://www.messenger.com/t/{chatbot.thread_id}/")
        self.login()

    def run(self):
        while True:
            self.driver.implicitly_wait(10000)
            try:
                self.wait_for_message()
                msg = self.get_latest_message()
            # self.wait_for_message()
            # message = self.get_latest_message()
            # print(f"{self._time} : waiting...")
            # self.send_message("Pybot: Online")
            finally:
                continue
        # print(f"element not found... any data?:\n> {self.driver}")
        # driver.quit()

    def select_input_box(self):

        self._wait.until(
            EC.presence_of_element_located((By.XPATH, INPUT_FIELD))
        )

    def get_latest_message(self):
        print("getting latest message...")
        return Message(self.driver.find_element(By.XPATH, '//div[@class="g5ia77u1 jwdofwj8 pby63qed"]'))

    def wait_for_message(self):
        self._message_wait.until(
            EC.presence_of_element_located((By.XPATH, MESSAGE_CONTAINER, self.number_of_messages_displayed()))
        )

    def number_of_messages_displayed(self):
        print(f"length of messages: {len(self.driver.find_elements(By.XPATH, MESSAGES_OTHERS))}")
        return len(self.driver.find_elements(By.XPATH, MESSAGES_OTHERS))

    def login(self):
        driver, chatbot = self.driver, self.chatbot

        # accept cookies
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "cookie_banner_title"))
        )
        # find login accept button and click it
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Accept All']"))
        )
        driver.find_element_by_xpath("//button[@title='Accept All']").click()

        # input account details
        login_input = driver.find_element_by_id("email")
        login_input.send_keys(chatbot.username)
        password_input = driver.find_element_by_id("pass")
        password_input.send_keys(chatbot.password)
        login_button = driver.find_element_by_id("loginbutton")
        login_button.click()

    def send_message(self, message):
        driver = self.driver
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, INPUT_FIELD))
            # or EC.presence_of_element_located((By.XPATH, "//div[@id='_1p1t _1p1u']")),
        )
        msg_input = driver.find_element_by_xpath(INPUT_FIELD)

        msg_input.send_keys(message)
        msg_input.send_keys(Keys.ENTER)
        print(f"message sent: {message}")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def wait_for_message(self):
        pass
