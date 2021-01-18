from chatbot import Chatbot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

my_group = "threadId"


class WebController:
    @staticmethod
    def send_message(driver, message):
        elem = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='_1mf _1mj']")),
        )
        msg_input = driver.find_element_by_xpath("//div[@class='_1mf _1mj']")
        msg_input.click()

        msg_input.send_keys(message)
        msg_input.send_keys(Keys.ENTER)
        print(f"message sent: {message}")

    def __init__(self, chatbot=Chatbot("ezelbot66@gmail.com", "lezetykurwo", my_group)):
        self.chatbot = chatbot
        print("init starts")
        self.driver = webdriver.Chrome()
        print(self.driver.name)
        self.driver.get("https://www.messenger.com/")

        while True:
            try:
                # accept cookies
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "cookie_banner_title"))
                )

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@id='u_0_g']"))
                )
                btn = self.driver.find_element_by_xpath("//button[@id='u_0_g']")
                btn.click()

                # select login input
                login_input = self.driver.find_element_by_id("email")
                login_input.send_keys(chatbot.username)
                password_input = self.driver.find_element_by_id("pass")
                password_input.send_keys(chatbot.password)
                login_button = self.driver.find_element_by_id("loginbutton")
                login_button.click()

                # elem = WebDriverWait(self.driver, 10).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, "j9ispegn pmk7jnqg k4urcfbm datstx6m lupvgy83 kr520xx4 mdpwds66 b2cqd1jy n13yt9zj eh67sqbx"))
                # )
                # i = self.driver.find_element_by_class_name("j9ispegn pmk7jnqg k4urcfbm datstx6m lupvgy83 kr520xx4 mdpwds66 b2cqd1jy n13yt9zj eh67sqbx")
                # i.click()

                # WebDriverWait(self.driver, 5).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, ""))
                # )

                # features_lock_error = WebDriverWait(driver, 5).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, "_1mf _1mj"))
                # )
                # ok = driver.find_element_by_class_name("_1mf _1mj")
                # ok.click()
                self.send_message(self.driver, "hi! I am gabe")
            finally:
                print(f"element not found... any data?: {self.driver}")
                # driver.quit()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def wait_for_message(self):
        pass
