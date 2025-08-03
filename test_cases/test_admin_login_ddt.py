import pytest
import time
from base_pages.Login_Admin_Page import LoginPage
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utilities

class Test_002_Admin_Login_DDt:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data/LoginData.xlsx"

    def test_valid_admin_login(self, setup):
        self.logger.info("************ Test Valid Admin Login Started *************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = LoginPage(self.driver)

        rows = excel_utilities.getRowCount(self.path, 'Sheet1')
        status_list = []

        for r in range(2, rows + 1):
            username = excel_utilities.readData(self.path, 'Sheet1', r, 1)
            password = excel_utilities.readData(self.path, 'Sheet1', r, 2)
            expected = excel_utilities.readData(self.path, 'Sheet1', r, 3)

            self.admin_lp.setUserName(username)
            self.admin_lp.setPassword(password)
            self.admin_lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if expected == "Pass":
                    status_list.append("Pass")
                    self.admin_lp.clickLogout()
                else:
                    status_list.append("Fail")
            else:
                if expected == "Pass":
                    status_list.append("Fail")
                else:
                    status_list.append("Pass")

        assert "Fail" not in status_list, f"DDT Failed: {status_list}"