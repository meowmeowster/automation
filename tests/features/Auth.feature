# -*- coding: utf-8 -*-
@smoke

#Background: Вход в браузер
#  Given Пусть пользователь запустил браузер

Feature: Смоук-тесты
  @auth
  Scenario: Смоук-тест авторизации
    Given Пусть пользователь открыл страницу "https://apparel-uk.local:9002/ucstorefront/en"