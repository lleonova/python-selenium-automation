# Created by username at 6/26/20
Feature: Test Scenarios for Amazon Shopping Cart functionality for Sign-out user

  Scenario:  Verify that clicking on the cart icon opens an empty Shopping Cart.
    Given Open Amazon page
    When Amazon Shopping Cart has 0 items
    And Click on Shopping Cart icon
    Then Verify that Amazon Cart is empty
