import json
import random
import unittest
from time import sleep
from selenium import webdriver
from time import gmtime, strftime
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class AngelAutomatization:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://angel.co/login")

    def log_in(self):
        driver = self.driver
        angel_email = "yaroslavyanko@gmail.com"
        angel_password = "852456753951angel"

        email_field_id = "user_email"
        password_field_id = "user_password"
        login_button_xpath = "//input[@value='Log In']"

        # webdriver's going to wait max 10 seconds for email's field, password field, login button to display
        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        password_field_element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(password_field_id))
        login_button_element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(login_button_xpath))

        email_field_element.clear()
        email_field_element.send_keys(angel_email)
        password_field_element.clear()
        password_field_element.send_keys(angel_password)
        login_button_element.click()

    def connect(self):
        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = self.driver
        connections = 0
        data = []

        # goes to recommended people page
        driver.get("https://angel.co/anna-shlepak/recommended_people")
        driver.implicitly_wait(3)

        connect_buttons = driver.find_elements_by_class_name(
            "shared-recommended_people")  # connect_button
        # for each connection
        for each in connect_buttons:
            connections += 1
            # try:
            #     con_id = each.driver.find_element_by_xpath("//a[@href]").get_attribure("href")
            #     con_name = each.find_element_by_class_name("details-title").text
            #     con_time = each.strftime("%Y-%m-%d_%H:%M:%S", gmtime())
            #     if con_time and con_id and con_name:
            #         data.append(
            #             [con_time, ' '.join(con_name.split(' ')[3:]), '{}'.format(con_id)])
            # except StaleElementReferenceException:
            #     pass
            try:
                button = each.find_element_by_link_text("Connect")
                # click connect
                button.click()
                # click confirm
                driver.find_element_by_link_text("Confirm").send_keys('\n')
                # wait for 2 seconds after connecting to a person
                driver.implicitly_wait(2)
            except NoSuchElementException:
                pass
            # add first 20-30 people from the list, then - break the loop
            if connections > random.randint(20, 30):
                break

        display.stop()
        return data

    # @staticmethod
    # def save_data(result):
    #     with open('angel_log.csv', 'a') as fl:
    #         for i in result:
    #             try:
    #                 fl.write('%s;%s; %s;\n' % (i[0], i[1], i[2]))
    #             except UnicodeEncodeError:
    #                 print('UnicodeEncodeError')

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    test = AngelAutomatization()
    test.log_in()
    test.connect()
    # test.save_data()
    test.tear_down()
