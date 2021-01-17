from chatbot import Chatbot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

my_group = "threadId"


class WebController:
    def send_message(self, driver, message):
        msg_input = driver.find_element_by_id("placeholder-fs2po")
        msg_input.click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "placeholder-fs2po"))
        )
        msg_input.send_keys(message)
        msg_input.send_keys(Keys.ENTER)
        print(f"message sent: {message}")

    def __init__(self, chatbot=Chatbot("ezelbot66@gmail.com", "lezetykurwo", my_group)):
        self.chatbot = chatbot
        print("init starts")
        driver = webdriver.Chrome()
        print(driver.name)
        driver.get("https://www.messenger.com/")

        while True:
            try:
                # accept cookies
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "cookie_banner_title"))
                )
                btn = driver.find_element_by_id('u_0_j')
                btn.click()

                # select login input
                login_input = driver.find_element_by_id("email")
                login_input.send_keys(chatbot.username)
                password_input = driver.find_element_by_id("pass")
                password_input.send_keys(chatbot.password)
                login_button = driver.find_element_by_id("loginbutton")
                login_button.click()

                # features_lock_error = WebDriverWait(driver, 5).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, "_1mf _1mj"))
                # )
                # ok = driver.find_element_by_class_name("_1mf _1mj")
                # ok.click()
                self.send_message(driver, "hi! I am gabe")
            finally:
                print(f"element not found... any data?: {driver}")
                # driver.quit()


def __enter__(self):
    pass


def __exit__(self, exc_type, exc_val, exc_tb):
    pass


def wait_for_message(self):
    pass
