#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import Engine
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.steps = Engine()


def after_all(context):
    context.browser.close()
