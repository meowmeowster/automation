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
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.opera.options import Options as OptionsOpera
from msedge.selenium_tools import EdgeOptions as OptionsEdge

browser = open(os.getcwd()+"/browser.txt").read()

if browser == "Chrome":
    options = OptionsChrome()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
elif browser == "Firefox":
    options = OptionsFirefox()
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)
elif browser == "Opera":
    options = OptionsOpera()
    options.add_argument("--headless")
    driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
elif browser == "Edge":
    options = OptionsEdge()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    driver = webdriver.Opera(executable_path=EdgeChromiumDriverManager().install(), options=options)
else:
    # Chrome driver by default
    options = OptionsChrome()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def unix():
    return sys.platform.startswith('linux') or sys.platform.startswith('darwin')


class Steps(unittest.TestCase):
    def is_unix(self):
        return unix()

    def stop_webdriver(self):
        driver.close()
        driver.quit()
