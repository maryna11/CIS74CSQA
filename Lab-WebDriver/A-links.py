# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "AA-T/AS-T Transfer Degrees" : "De Anza College :: Transfer Degrees :: AA-T/AS-T Degree Overview", 
            "AB540 (Undocumented Students)" : "De Anza College :: Outreach :: AB540 Guide for Undocumented Immigrant Students",
            "About De Anza" : "De Anza College :: About De Anza :: Home",
            "Academic Calendar" : "De Anza College :: Academic Calendar :: Home",
            "Academic Freedom Policy" : "De Anza College :: About De Anza :: Academic Freedom",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
