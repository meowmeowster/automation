#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..framework.main import *


class Cases(Steps):
    def test_smoke_auth(self):
        driver = start_driver()
        Steps.get_address(self, driver, "https://apparel-uk.local:9002/ucstorefront/en")
        Steps.smart_action(self, driver, "class_name", "liOffcanvas", "click")
        Steps.smart_action(self, driver, "id", "j_username", "type", "test39@test.com")
        Steps.smart_action(self, driver, "id", "j_password", "type", "123456")
        Steps.smart_action(self, driver, "class_name", "btn-primary", "click")
        Steps.smart_read(self, driver, "class_name", "js-logged_in", "Welcome test39")
        stop_driver(driver)

