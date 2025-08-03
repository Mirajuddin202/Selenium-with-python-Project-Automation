import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import LoginPage
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_001_Admin_Login:
    admin_page_url=Read_Config.get_admin_page_url()
    username=Read_Config.get_usermane()
    password=Read_Config.get_password()
    invalid_username=Read_Config.get_invalid_usermane()
    logger= Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title(self,setup):
        self.logger.info("************ Test_001_Admin Login **************")
        self.logger.info("************ Admin Login Page Title *************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        act_title=self.driver.title
        exp_title="nopCommerce demo store. Login"
        if act_title==exp_title:
            self.logger.info("************ Test Title Match *************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title.png")
            self.logger.info("************ Test Title Not Match *************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("************ Test Valid Admin Login Started *************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=LoginPage(self.driver)
        self.admin_lp.setUserName(self.username)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogin()
        act_dashboard_text=self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashboard_text=="Dashboard":
            self.logger.info("************ Dashboard text Found *************")
            assert  True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("************ test_invalid_admin_login Started*************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=LoginPage(self.driver)
        self.admin_lp.setUserName(self.invalid_username)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogout()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message =="No customer account found" :
            self.logger.info("************ test_invalid_admin_login error messeage matched *************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False
