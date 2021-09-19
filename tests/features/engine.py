#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


def unix():
    return sys.platform.startswith("linux") or sys.platform.startswith("darwin")


class Engine(Browser):
    def get_address(self, address):
        try:
            Browser.driver.get(address)
        except TimeoutException:
            self.fail("Exception while trying to connect to " + address)

    def smart_wait(self, visibility, length=3, is_negative=False):
        try:
            wait = WebDriverWait(Browser.driver, length)
            wait.until(visibility)
        except TimeoutException:
            if not is_negative:
                self.fail("Timeout exception while looking for element")

    def smart_search(self, locator, content, is_negative=False):
        try:
            if locator == "class_name":
                visibility = EC.visibility_of_element_located((By.CLASS_NAME, content))
                Engine.smart_wait(self, visibility, is_negative)
                return Browser.driver.find_element_by_class_name(content)
            elif locator == "id":
                visibility = EC.visibility_of_element_located((By.ID, content))
                Engine.smart_wait(self, visibility, is_negative)
                return Browser.driver.find_element_by_id(content)
            else:
                return None
        except Exception:
            if not is_negative:
                self.fail("Exception on " + locator + " search of " + content)
            else:
                pass

    def smart_action(self, locator, content, action, source=None):
        element = Engine.smart_search(self, locator, content)
        if action == "click":
            element.click()
        elif action == "type":
            element.send_keys(source)
        else:
            return None

    def smart_read(self, locator, content, data, is_placeholder=False, is_empty=False):
        element = Engine.smart_search(self, locator, content)
        source = element.text
        if is_empty:
            return source == ""
        else:
            return data.lower().strip() in source.lower().strip()
