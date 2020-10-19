from selenium.webdriver.support.ui import Select
import time


class AddCustomer():

    lnk_customers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnk_customers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    btnCustomerinfo_xpath = "//div[@class='icon-container']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitemAdminstrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnk_customers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_customers_menuitem_xpath).click()

    def clickonCustomerinfo(self):
        self.driver.find_element_by_xpath(self.btnCustomerinfo_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.txt_FirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_xpath(self.txt_LastName_xpath).send_keys(lastName)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDob(self, Dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(Dob)

    def setCompanyName(self, Company):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(Company)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(5)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath).click()
        elif role == "Adminstrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdminstrators_xpath).click()
        elif role == "Guests":
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath).click()
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        self.driver.execute_script("arguments[0].click;", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, AdminContent):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(AdminContent)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
