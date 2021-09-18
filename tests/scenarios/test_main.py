#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..framework.main import Steps


class Cases(Steps):
    def test_main(self):
        #assert(self.is_unix() == True)
        self.stop_webdriver()
