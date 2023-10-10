import time

from selenium.webdriver.common.by import By


class HomePage:
    button_buyticket_xpath = "//a[contains(text(),'Buy Ticket')]"

    def __init__(self, driver):
        self.driver = driver

    def clickbuyticket(self):
        button_buyticket = self.driver.find_element(By.XPATH, self.button_buyticket_xpath)
        button_buyticket.click()
        time.sleep(5)