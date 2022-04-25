from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

# Imports for general selenium functionality.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import time
import getpass
import datetime
import os
import sys
import platform


def login (username_phone_number, password, driver):
#     return true or false
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "loginKey")))


    # If loginKey is present, the element with attribute name password also exist,
    # we set the value of this element to be the username_email and password respectively.
    driver.find_element_by_name("loginKey").send_keys(username_phone_number)
    driver.find_element_by_name("password").send_keys(password)


    # Wait until login element with a specific class value is clickable.
    # Using XPATH format:
    # "//element_name[@atteibute_name=value]"
    # Example: <button class="_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='_1ruZ5a _3Nrkgj _3kANJY _1IRuK_ hh2rFL _3_offS']")))

    # If the button exists, we click it. This emulates login button with the values we provided.
    driver.find_element_by_xpath("//button[@class='_1ruZ5a _3Nrkgj _3kANJY _1IRuK_ hh2rFL _3_offS']").click()

    # The page will load. The element with attribute name "autocomplete" and value "one-time-code" should appear.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="one-time-code"]')))

    # We get the html source of the current page and
    # we chekc if the text "Your verification code is sent by SMS to your phone" appears.

    html_source = driver.page_source

    if "Your verification code is sent by SMS to your phone" in html_source:
        return True

    return False

def mobile_verification(verification_number, driver):
    """
        This function will be called if you the login to website was success and we need
        to enter verification code.
        """

    # Wait for the onetimecode element to appear which can be found with input element with autocomplete name attribute
    # then send verfication number in it.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="one-time-code"]')))
    driver.find_element_by_xpath('//input[@autocomplete="one-time-code"]').send_keys(verification_number)

    # Wait for the verification button to appear then perform submit action.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='_1ruZ5a _3Nrkgj _3kANJY _1IRuK_ X27k2C hh2rFL _3_offS']")))
    driver.find_element_by_xpath("//button[@class='_1ruZ5a _3Nrkgj _3kANJY _1IRuK_ X27k2C hh2rFL _3_offS']").click()


def clear_screen():
    os_type = platform.system()

    if os_type == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():

    clear_screen()

    # chrome_options = Options()
    # chrome_options.headless = True

    firefox_options = Options()
    firefox_options.add_argument("--disable-extensions")

    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=)

    driver = webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)
    driver.get("https://seller.shopee.co.id/account/signin?next=%2F")

    try:
        print("Enter your email address or phone number: ")
        username_email = input("> ")

        print("Enter your password (it won't appear in the terminal): ")
        password = getpass.getpass("> ")

    #     if login succeed:

        if login(username_email, password, driver):
            # If login success, mobile verification is required.
            print("OTP sent in your mobile number, please wait for it to be received.")
            print("Enter verification code sent in your mobile number:")
            mobile_verification_number = input("> ")

            print("Verifying OTP...")
            mobile_verification(mobile_verification_number, driver)
            print("OTP correct, please wait...")


    except Exception as exp:
        print("An error has occured.")
        print(str(exp))

    finally:
        print("Program Ended.")
        driver.close()

