# -*- coding: utf-8 -*-

Feature: Authorization for plain user

  @auth @smoke
  Scenario: Auth, positive
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "liOffcanvas"
    Then user typed "test39@test.com" into "id" called "j_username"
    Then user typed "123456" into "id" called "j_password"
    Then user clicked on "class_name" called "btn-primary"
    Then user saw the text "Welcome test39" in "class_name" called "js-logged_in"

  @auth
  Scenario: Auth, negative
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "liOffcanvas"
    Then user typed "test39@test.com" into "id" called "j_username"
    Then user typed "654321" into "id" called "j_password"
    Then user clicked on "class_name" called "btn-primary"
    Then user saw the text "Your username or password was incorrect." in "class_name" called "getAccAlert"
    Then the "class_name" called "js-logged_in" is not present
