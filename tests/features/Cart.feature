# -*- coding: utf-8 -*-

Feature: Shopping cart

  @cart @smoke
  Scenario: Open and close cart
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "nav-cart"
    Then user saw the text "Bag" in "class_name" called "headline-text"
    Then user saw the text "Continue Shopping" in "class_name" called "js-mini-cart-close-button"
    Then user clicked on "id" called "cboxClose"
    Then the "class_name" called "js-mini-cart-close-button" is not present

  @cart
  Scenario: Open and continue shopping
    Given user opened "https://apparel-uk.local:9002/ucstorefront/en"
    Then user clicked on "class_name" called "nav-cart"
    Then user saw the text "Bag" in "class_name" called "headline-text"
    Then user saw the text "Continue Shopping" in "class_name" called "js-mini-cart-close-button"
    Then user clicked on "class_name" called "js-mini-cart-close-button"
    Then the "class_name" called "js-mini-cart-close-button" is not present