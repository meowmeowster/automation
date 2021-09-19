# -*- coding: utf-8 -*-
@smoke

#Background: Вход в браузер
#  Given Пусть пользователь запустил браузер

Feature: Smoke
  @auth
  Scenario: Auth smoke
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "liOffcanvas"
    Then user typed "test39@test.com" into "id" called "j_username"