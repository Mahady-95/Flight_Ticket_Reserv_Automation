import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TicketBookingPage:

    rd_visaticket_id = "product_549"
    txt_firstname_xpath="//input[@id='travname']"
    txt_lastname_xpath="//input[@id='travlastname']"
    tbl_dob_xpath="//input[@id='dob']"
    tbl_drp_month_xpath="//select[@aria-label='Select month']"
    tbl_drp_year_xpath="//select[@aria-label='Select year']"
    all_dates_xpath = "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a"
    rd_male_id="sex_1"
    #rd_female_id="sex_2"
    rd_triptype_xpath="//label[contains(text(),'One Way')]"
    txt_fromcity_xpath="//input[@id='fromcity']"
    txt_tocity_xpath="//input[@id='tocity']"
    tbl_departure_xpath="//input[@id='departon']"
    txt_phone_xpath="//input[@id='billing_phone']"
    txt_email_xpath="//input[@id='billing_email']"
    txt_billing_country_xpath="//select[@id='billing_country']"
    txt_bstreet_address_name="billing_address_1"
    txt_bsuburb_xpath="//input[@id='billing_city']"
    b_state_xpath="//select[@id='billing_state']"
    txt_bpostcode_xapth="//input[@id='billing_postcode']"
    rd_paypal_xpath="//input[@id='payment_method_paypal']"
    #rd_debitcard_xapth="//label[contains(text(),'Debit and Credit Card')]"
    button_proceedtopay="//button[@id='place_order']"


    def __init__(self, driver):
        self.driver = driver
    def selectradiobutton(self):
        radio_button=self.driver.find_element(By.ID, self.rd_visaticket_id)
        if radio_button.is_selected():
            print("radio button is selected")
        else:
            print("radio button is not selected")
        if not radio_button.is_selected():
            radio_button.click()
        # Verify if the radio button is selected after clicking
        if radio_button.is_selected():
            print("Radio button has been selected")
    def setfirstname(self):
        firstnane=self.driver.find_element(By.XPATH, self.txt_firstname_xpath)
        firstnane.send_keys("Ashek")
    def setlastname(self):
        lastname=self.driver.find_element(By.XPATH, self.txt_lastname_xpath)
        lastname.send_keys("Mahady")
    def setdob(self):
        self.driver.find_element(By.XPATH, self.tbl_dob_xpath).click()
        date_pickermonth = Select(self.driver.find_element(By.XPATH, self.tbl_drp_month_xpath))
        date_pickermonth.select_by_visible_text("Jan")

        date_pickeryear = Select(self.driver.find_element(By.XPATH, self.tbl_drp_year_xpath))
        date_pickeryear.select_by_visible_text("1998")

        all_dates = self.driver.find_elements(By.XPATH, self.all_dates_xpath)

        for date in all_dates:
            if date.text == "11":
                date.click()
                break
    def selectsex(self):
        rd_male=self.driver.find_element(By.ID, self.rd_male_id)
        if rd_male.is_selected():
            print("radio button male selected")
        else:
            print("radio button male is not selected")
        if not rd_male.is_selected():
            rd_male.click()
        if rd_male.is_selected():
            print("male is selected")
    def selecttriptype(self):
        rd_male=self.driver.find_element(By.XPATH, self.rd_triptype_xpath)
        if rd_male.is_selected():
            print("radio button male selected")
        else:
            print("radio button male is not selected")
        if not rd_male.is_selected():
            rd_male.click()
        if rd_male.is_selected():
            print("Radio button has selected")
    def setfromcity(self):
        from_city=self.driver.find_element(By.XPATH,self.txt_fromcity_xpath)
        from_city.send_keys("Savar")

    def settocity(self):
        to_city = self.driver.find_element(By.XPATH, self.txt_tocity_xpath)
        to_city.send_keys("Canada")
    def setdeparture(self):
        self.driver.find_element(By.XPATH, self.tbl_departure_xpath).click()
        date_pickermonth = Select(self.driver.find_element(By.XPATH, self.tbl_drp_month_xpath))
        date_pickermonth.select_by_visible_text("Nov")

        date_pickeryear = Select(self.driver.find_element(By.XPATH, self.tbl_drp_year_xpath))
        date_pickeryear.select_by_visible_text("2023")

        all_dates = self.driver.find_elements(By.XPATH, self.all_dates_xpath)

        for date in all_dates:
            if date.text == "11":
                date.click()
                break
    def setphone(self):
        b_phone=self.driver.find_element(By.XPATH, self.txt_phone_xpath)
        b_phone.send_keys("01700000011")
    def setemail(self):
        b_email=self.driver.find_element(By.XPATH, self.txt_email_xpath)
        b_email.send_keys("ash@gmail.com")

    def setbillingcountry(self):
        dropdown = self.driver.find_element(By.XPATH, self.txt_billing_country_xpath)
        # Create a Select object from the dropdown element
        select = Select(dropdown)
        select.select_by_visible_text("Australia")
    def setbillingstreet(self):
        b_street=self.driver.find_element(By.NAME,self.txt_bstreet_address_name)
        b_street.send_keys("1A")
    def setbillingcity(self):
        b_city=self.driver.find_element(By.XPATH,self.txt_bsuburb_xpath)
        b_city.send_keys("Wooden Spice")
    def setbillingstate(self):
        dropdown = self.driver.find_element(By.XPATH, self.b_state_xpath)
        # Create a Select object from the dropdown element
        select = Select(dropdown)
        select.select_by_visible_text("Tasmania")
    def setbillingpostcode(self):
        b_postcode=self.driver.find_element(By.XPATH,self.txt_bpostcode_xapth)
        b_postcode.send_keys("19009")
    def selectpaymentmethod(self):
        rd_male=self.driver.find_element(By.XPATH, self.rd_paypal_xpath)
        if rd_male.is_selected():
            print("radio button paypal selected")
        else:
            print("radio button paypal is not selected")
        if not rd_male.is_selected():
            rd_male.click()
        if rd_male.is_selected():
            print("Radio button paypal has is selected")
    def clickproceedtopay(self):
        btn_pay=self.driver.find_element(By.XPATH,self.button_proceedtopay)
        btn_pay.click()






