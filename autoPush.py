import time
from selenium.webdriver.common.action_chains import ActionChains
from utilities import timestamp

def directToClick(driver):
    try:
        directToItem = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[3]/ul/li[1]/a').click()

    except Exception as e:
        directHomePage = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[1]/a').click()
        directToItem = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[3]/ul/li[1]/a/span').click()
        print(e)

    time.sleep(5)

    try:
        directToSquare = driver.find_element_by_xpath \
            ('//html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/i').click()
    except Exception as e:
        close_prompt = driver.find_element_by_xpath \
            ("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div[2]/div").click()
        print(e)


def clickMoreAndPush(driver):
    hover = ActionChains(driver)
    datas = ""
    for i in range(1, 6):
        more = driver.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[1]/div/div[{}]/div/div[6]/div[2]/div'.format
             (i))
        pushIconText = driver.find_element_by_xpath('/html/body/div[{}]/ul/li[4]/div/div'.format(i + 4))
        hover = ActionChains(driver)
        hover.move_to_element(more).pause(3)
        hover.click(pushIconText)
        hover.perform()
        currentStr = "Time:{} this is {} times click remain time of text: {}\n".format(timestamp(), i, pushIconText.text)
        print(currentStr)
    return datas
