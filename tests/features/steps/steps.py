#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *


@Given(u"^Пусть пользователь открыл страницу [\'\"]{address}[\'\"]$")
def step_impl(context, address):
    context.get_address(address)




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