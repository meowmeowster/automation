# -*- coding: utf-8 -*-

Feature: Smoke
  @header @smoke
  Scenario: Cookie
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user saw the text "We use cookies" in "id" called "js-cookie-notification"
    Then user clicked on "class_name" called "js-cookie-notification-accept"
    Then the "class_name" called "js-cookie-notification-accept" is not present