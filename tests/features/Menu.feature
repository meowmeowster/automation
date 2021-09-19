# -*- coding: utf-8 -*-

Feature: Main menu elements

  @menu @smoke
  Scenario: Main page
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then the current url is "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "js-site-logo"
    Then the current url is "https://apparel-uk.local:9002/ucstorefront/en"