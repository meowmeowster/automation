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


def start_driver():
    browser = open(os.getcwd() + "/browser.txt").read()

    desired_capabilities = {
        "acceptInsecureCerts": True
    }

    if browser == "Chrome":
        options = OptionsChrome()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--window-size=1920,1080')
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == "Firefox":
        options = OptionsFirefox()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--window-size=1920,1080')
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   firefox_options=options, firefox_profile=profile)
    elif browser == "Opera":
        options = OptionsOpera()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Opera(executable_path=OperaDriverManager().install(),
                                 options=options, desired_capabilities=desired_capabilities)
    elif browser == "Edge":
        options = OptionsEdge()
        options.use_chromium = True
        options.add_argument("headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--window-size=1920,1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Opera(executable_path=EdgeChromiumDriverManager().install(),
                                 options=options, desired_capabilities=desired_capabilities)
    else:
        # Chrome driver by default
        options = OptionsChrome()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--window-size=1920,1080')
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    return driver


def stop_driver(driver_instance):
    driver_instance.close()
    driver_instance.quit()


def unix():
    return sys.platform.startswith("linux") or sys.platform.startswith("darwin")


class Steps(unittest.TestCase):

    def get_address(self, driver, address):
        try:
            driver.get(address)
        except TimeoutException:
            stop_driver(driver)
            self.fail("Exception while trying to connect to " + address)

    def login(self, driver, login, password):
        try:
            element = driver.find_elements_by_class_name('1').__getitem__(0)
            element.send_keys(login)
            element = driver.find_elements_by_class_name('2').__getitem__(1)
            element.send_keys(password)

            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '3')))
            element = driver.find_element_by_class_name('4')
            element.click()
        except TimeoutException:
            stop_driver(driver)
            self.fail("Timeout exception while logging in")

    def smart_wait(self, driver, visibility, length=3):
        try:
            wait = WebDriverWait(driver, length)
            wait.until(visibility)
        except TimeoutException:
            stop_driver(driver)
            self.fail("Timeout exception while looking for element")

    def smart_search(self, driver, locator, context):
        try:
            if locator == "class_name":
                visibility = EC.visibility_of_element_located((By.CLASS_NAME, context))
                Steps.smart_wait(self, driver, visibility)
                return driver.find_element_by_class_name(context)
            elif locator == "id":
                visibility = EC.visibility_of_element_located((By.ID, context))
                Steps.smart_wait(self, driver, visibility)
                return driver.find_element_by_id(context)
            else:
                return None
        except Exception:
            stop_driver(driver)
            self.fail("Exception on " + locator + " search of " + context)

    def smart_action(self, driver, locator, context, action, source=None):
        element = Steps.smart_search(self, driver, locator, context)
        if action == "click":
            element.click()
        elif action == "type":
            element.send_keys(source)
        else:
            return None
