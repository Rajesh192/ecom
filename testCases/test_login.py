import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setUp):

        self.logger.info("*********************Test_Login_1**********************************")
        self.logger.info("*********************Verifying_Login_Page_Title**********************************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title =="Your store. Login":
            self.logger.info("*********************LoginPage_Title_Test_Passed**********************************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********************LoginPage_Title_Tst_Failed**********************************")
            self.driver.save_screenshot("loginPage.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUp):

        self.logger.info("*********************Test_Login_2**********************************")
        self.logger.info("*********************Verifying_Home_Page_Title**********************************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_titile = self.driver.title
        if act_titile == "Dashboard / nopCommerce administration":
            self.logger.info("*********************HomePage_Title_Test_Passed**********************************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..//Reorts/Screen.png")
            self.logger.info("*********************HomePage_Title_Test_Failed**********************************")
            self.driver.close()
            assert False



