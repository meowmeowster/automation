#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..framework.main import *


class Cases(Steps):
    def test_smoke(self):
        driver = start_driver()
        Steps.get_address(self, driver, "https://apparel-uk.local:9002/ucstorefront/en")
        Steps.smart_action(self, driver, "class_name", "liOffcanvas", "click")
        stop_driver(driver)

