# -*- coding: utf-8 -*-
@smoke

#Background: Вход в браузер
#  Given Пусть пользователь запустил браузер

Feature: Smoke
  @auth
  Scenario: Auth smoke
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user performed "click" action on "class_name" called "liOffcanvas"