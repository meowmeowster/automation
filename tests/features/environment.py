#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.framework.main import *


def before_all(context):

    context.steps = Steps()
    context.steps.start_driver()


def after_all(context):
    context.steps.stop_driver()