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
            "Flu Information and Updates" : "De Anza College :: Flu Information and Updates :: Home",
            "Foothill College" : "Foothill College is a 2-year community college providing a wide range of educational opportunities for all.",
            "Foothill-De Anza District" : "Welcome to Foothill-De Anza",
            "French Department" : "De Anza College :: French :: Home",
            "Friends of De Anza" : "De Anza College :: Friends :: Home",
            "Gainful Employment Disclosure" : "De Anza College :: Workforce Education :: Gainful Employment Disclosure",
            "General Subjects Tutoring" : "De Anza College :: General Subjects Tutoring :: Home",
            "Geography Department" : "De Anza College :: Geography :: Home",
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
