import time

from pageObjects.HomePage import HomePage

from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig
from pageObjects.TicketBookingPage import TicketBookingPage

class TestTicketBookingPage002:
    baseUrl=ReadConfig.getApplicationURL()

    logger = LogGen.logegn()
    def test_TicketBoookingPage(self, setUp):
        self.driver=setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.hp=HomePage(self.driver)
        # Scroll down by 500 pixels
        self.hp.clickbuyticket()
        self.logger.info("**** Starting testing (TestTicketBookingPage002) ****")
        self.tbkp=TicketBookingPage(self.driver)
        act_title=self.driver.title
        exp_title="Dummy ticket for applying visa - Verifiable flight reservation for embassy"
        if act_title==exp_title:
            assert True
            self.logger.info("***** We are in ticket reservation page (verified) *****")
        else:
            assert False
        self.driver.execute_script("window.scrollBy(0, 400);")
        self.logger.info("**** Choosing the correct option ****")
        self.tbkp.selectradiobutton()
        time.sleep(3)
        self.logger.info("**** Providing passenger details ****")
        self.tbkp.setfirstname()
        self.tbkp.setlastname()
        self.tbkp.setdob()
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(2)
        self.tbkp.selectsex()
        self.tbkp.selecttriptype()
        self.tbkp.setfromcity()
        self.tbkp.settocity()
        self.driver.execute_script("window.scrollBy(0, 400);")
        self.tbkp.setdeparture()
        self.driver.execute_script("window.scrollBy(0, 700);")
        self.logger.info("**** Providing billing details ****")
        self.tbkp.setphone()
        self.tbkp.setemail()
        self.tbkp.setbillingcountry()
        self.tbkp.setbillingstreet()
        self.tbkp.setbillingcity()
        self.tbkp.setbillingstate()
        self.tbkp.setbillingpostcode()
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.logger.info("**** Selecting payment method ****")
        self.tbkp.selectpaymentmethod()
        time.sleep(3)
        self.tbkp.clickproceedtopay()
        print("done")

        time.sleep(10)
        self.driver.close()
        self.logger.info("**** This is the end of testing (TestTicketBookingPage002) **** ")
#pytest -s -v --html=reports\report.html testCases/test_TicketBookingPage.py --browser chrome

