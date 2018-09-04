import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SortingByDropdownMenu(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'test'
        desired_caps['app'] = PATH('./apk/moviesapp.apk')
        desired_caps['autoGrantPermissions'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_most_popular(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@clickable,'true')]").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[contains(@index,0)]").click() #send_keys('joanne-foo@ambankgroup.com')
        sleep(2)
    
    def test_top_rated(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@clickable,'true')]").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[contains(@index,1)]").click() #send_keys('joanne-foo@ambankgroup.com')
        sleep(2)
    
    def tearDown(self):
        # end the session
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SortingByDropdownMenu)
    unittest.TextTestRunner(verbosity=2).run(suite)