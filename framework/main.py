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

capabilities = {
    "browserName": "chrome",
    "version": "85.0",
    "enableVNC": True,
    "enableVideo": False
}
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    desired_capabilities=capabilities)


def unix():
    return sys.platform.startswith('linux') or sys.platform.startswith('darwin')


class Steps(unittest.TestCase):
    def is_unix(self):
        return unix()

