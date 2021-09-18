#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..framework.main import *


class Cases(Steps):
    def test_main(self):
        driver = start_driver()
        Steps.get_address(self, driver, "https://apparel-uk.local:9002/ucstorefront/en")
        stop_driver(driver)

