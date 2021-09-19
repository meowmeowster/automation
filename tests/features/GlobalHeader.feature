# -*- coding: utf-8 -*-

Feature: Header elements

  @header @smoke
  Scenario: Cookie
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user saw the text "We use cookies" in "id" called "js-cookie-notification"
    Then user clicked on "class_name" called "js-cookie-notification-accept"
    Then the "class_name" called "js-cookie-notification-accept" is not present

  @header @smoke
  Scenario: Search
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user saw the text "" in "id" called "js-site-search-input"
    Then user clicked on "class_name" called "glyphicon-search"
    Then the "class_name" called "results" is not present
    Then user saw the text "" in "id" called "js-site-search-input"
    Then user typed "123" into "id" called "js-site-search-input"
    Then user clicked on "class_name" called "glyphicon-search"
    Then user saw the text "You searched for" in "class_name" called "results"
