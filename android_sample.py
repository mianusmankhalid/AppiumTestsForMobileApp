import os
from time import sleep
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CheckingGender(unittest.TestCase):
    # reportDirectory = 'reports'
    # reportFormat = 'xml'
    # dc = {}
    # testName = 'CheckingGender'
    # driver = None

    def setUp(self):
        # self.dc['reportDirectory'] = self.reportDirectory
        # self.dc['reportFormat'] = self.reportFormat
        # self.dc['testName'] = self.testName
        # self.dc['udid'] = ''
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'ReactNative8_0'
        desired_caps['app'] = PATH('app-release.apk')
        desired_caps['autoGrantPermissions'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    
    # def setUp(self):
    #     desired_caps = {}
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '8.0'
    #     desired_caps['deviceName'] = 'ReactNative8_0'
    #     desired_caps['app'] = PATH(
    #         'app-release.apk'
    #     )

    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testCheckingGender(self):
        #WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="edittext_signin_username"]')))
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='CONTINUE']").click()
        #sleep(1)
        self.driver.find_element_by_xpath("//*[@id='edittext_signin_password']").click() #send_keys('joanne-foo@ambankgroup.com')
        #self.driver.find_elements_by_xpath('//android.widget.TextView').send_keys('joanne-foo@ambankgroup.com')
        #self.driver.find_element_by_xpath("//*[@id='edittext_signin_username']").send_keys('joanne-foo@ambankgroup.com')
        #self.driver.findElement(By.xpath("//*[@id='edittext_signin_username']")).send_keys('joanne-foo@ambankgroup.com')
        
        # WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="edittext_signin_password"]')))
        # self.driver.find_element_by_xpath("xpath=//*[@id='edittext_signin_password']").send_keys('admin007')
        # WebDriverWait(self.driver, 1).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text="Sign In"]')))
        # self.driver.find_element_by_xpath("xpath=//*[@text='Sign In']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@id='imageView_more']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='Profile']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='Personal Details']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='Female']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@id='imageView_more']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='Log out']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='YES']").click()

    def tearDown(self):
        # end the session
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckingGender)
    unittest.TextTestRunner(verbosity=2).run(suite)