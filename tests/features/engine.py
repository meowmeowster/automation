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
            Browser.close()
            self.fail("Exception while trying to connect to " + address)

    def smart_wait(self, visibility, length=3):
        try:
            wait = WebDriverWait(Browser.driver, length)
            wait.until(visibility)
        except TimeoutException:
            Browser.close()
            self.fail("Timeout exception while looking for element")

    def smart_search(self, locator, context):
        try:
            if locator == "class_name":
                visibility = EC.visibility_of_element_located((By.CLASS_NAME, context))
                Engine.smart_wait(self, visibility)
                return Browser.driver.find_element_by_class_name(context)
            elif locator == "id":
                visibility = EC.visibility_of_element_located((By.ID, context))
                Engine.smart_wait(self, visibility)
                return Browser.driver.find_element_by_id(context)
            else:
                return None
        except Exception:
            Browser.close()
            self.fail("Exception on " + locator + " search of " + context)

    def smart_action(self, locator, context, action, source=None):
        element = Engine.smart_search(self, locator, context)
        if action == "click":
            element.click()
        elif action == "type":
            element.send_keys(source)
        else:
            return None

    def smart_read(self, locator, context, data):
        element = Engine.smart_search(self, locator, context)
        return data.lower().strip() in element.text.lower().strip()