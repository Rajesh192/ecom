import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_ddt_login:
    baseUrl = ReadConfig.getApplicationURL()
    path = "C:\\Users\\rvanacharla\\workspace_python\\ecom\\TestData\\LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setUp):

        self.logger.info("*********************Test_Login_2_DDT**********************************")
        self.logger.info("*********************Verifying_Home_Page_Title**********************************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("print Number of rows in Excel file is :", self.rows)

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.result = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_titile = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_titile == exp_title:
                if self.result == "pass":
                    self.logger.info("*********************HomePage_Title_Test_Passed********************************")
                    self.lp.clickLogout()

                elif self.result == "fail":
                    self.logger.info("*********************HomePage_Title_Test_Failed********************************")
                    self.lp.clickLogout()

            elif act_titile != exp_title:
                if self.result == "pass":
                    self.logger.info("*********************HomePage_Title_Test_Failed********************************")

                elif self.result == "fail":
                    self.logger.info("*********************HomePage_Title_Test_Passed********************************")

        self.logger.info("*******End of DTT Test Cases********")
        self.logger.info("**********Completion of Test_Login_2_DDT******")
