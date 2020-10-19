import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
import time
@pytest.mark.sanity
class Test_003_add_Customer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setUp):
        self.logger.info("*********************Test_Login_3**********************************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("**************Login Successful *************")
        self.logger.info("***************Starting Add Customer Test*************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(5)
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickOnAddNew()
        self.addCust.clickonCustomerinfo()
        self.logger.info("*******Providing Customer Details*************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Rajesh")
        self.addCust.setLastName("Vanacharla")
        self.addCust.setGender("Male")
        self.addCust.setDob("12/04/1998")
        self.addCust.setCompanyName("BCT")
        self.addCust.setCustomerRoles("Vendors")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This is for Testing...")
        self.addCust.clickOnSave()

        self.logger.info("******** Saving Customer Details*********")
        self.logger.info("********Add Customer Validation Started*****")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("*********Add Customer Test Passed*****")
        else:
            self.driver.save_screenshot("AddCustomerFailed.png")
            self.logger.info("*********Add Customer Test Failed*****")
            assert True == False

        self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
