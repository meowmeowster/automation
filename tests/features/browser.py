#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.opera.options import Options as OptionsOpera
from msedge.selenium_tools import EdgeOptions as OptionsEdge


class Browser(object):

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

    def close(context):
        context.driver.close()
        context.driver.quit()
