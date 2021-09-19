#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *


@Given('user opened "{address}"')
def step_impl(context, address):
    context.steps.get_address(address)

@Then('user clicked on "{locator}" called "{content}"')
def step_impl(context, locator, content):
    context.steps.smart_action(locator, content, "click")

@Then('user typed "{source}" into "{locator}" called "{content}"')
def step_impl(context, locator, content, source):
    context.steps.smart_action(locator, content, "type", source)

@Then('user saw the text "{data}" in "{locator}" called "{content}"')
def step_impl(context, locator, content, data):
    context.steps.smart_read(locator, content,  data)


#@step(u'run in parallel "{feature}" "{scenario}"')
#def step_impl(context, feature, scenario):
#    t = threading.Thread(
#        name='run test parallel',
#        target=parallel_executor,
#        args=[context, feature, scenario])
#        #args=[context, 'parallel_actions.feature', 'Make Cab-Cab communication'])
#    t.start()


#def parallel_executor(context, feature_name, scenario):
#    os.chdir(testenv.PARALLEACTIONS_PATH)
#    behave_main('-i "{}" -n "{}" --no-capture --no-skipped'.format(feature_name, scenario))