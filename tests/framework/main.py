#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--headless")
options.headless = True

#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)

def unix():
    return sys.platform.startswith('linux') or sys.platform.startswith('darwin')


class Steps(unittest.TestCase):
    def is_unix(self):
        return unix()

    def stop_webdriver(self):
        driver.close()
        driver.quit()
