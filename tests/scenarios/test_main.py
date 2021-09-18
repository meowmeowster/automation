#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.framework.main import Steps


class Cases(Steps):
    def test_main(self):
        assert(self.is_unix() == True)
