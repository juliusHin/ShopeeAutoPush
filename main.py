# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from login import *
from utilities import *
import autoPush
import getpass

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():

    clear_screen()

    # chrome_options = Options()
    # chrome_options.headless = True

    firefox_options = Options()
    # firefox_options.add_argument("--disable-extensions")
    firefox_options.add_argument("--start-maximized")
    # firefox_options.headless = True

    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=)

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    driver.get("https://seller.shopee.co.id/account/signin?next=%2F")



    try:
        print("Enter your email address or phone number: ")
        # username_email = input("> ")

        print("Enter your password (it won't appear in the terminal): ")
        # password = getpass.getpass("> ")

        username_email = "081387676573"
        password = "Paul_0999"

    #     if login succeed:
        all_product_url = "https://seller.shopee.co.id/portal/product/list/all"
        if login(username_email, password, driver):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "list-panel")))

            next_page = driver.find_element(by=By.XPATH, value="//button[@class='shopee-button shopee-button--small shopee-button--frameless shopee-button--block shopee-pager__button-next']")
            prev_page = driver.find_element(by=By.XPATH, value="//button[@class='shopee-button shopee-button--small shopee-button--frameless shopee-button--block shopee-pager__button-prev']")
            # If login success, mobile verification is required.
            # print("OTP sent in your mobile number, please wait for it to be received.")
            # print("Enter verification code sent in your mobile number:")
            # mobile_verification_number = input("> ")
            #
            # print("Verifying OTP...")
            # mobile_verification(mobile_verification_number, driver)
            # print("OTP correct, please wait...")


    except Exception as exp:
        print("An error has occured.")
        print(str(exp))

    finally:
        print("Program Ended.")
        driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


