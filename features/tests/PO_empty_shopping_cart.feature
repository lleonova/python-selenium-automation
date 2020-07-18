# Created by username at 7/17/20
Feature: Test Scenarios for Amazon Shopping Cart functionality for Sign-out user

  Scenario:  Verify that clicking on the cart icon opens an empty Shopping Cart.
    Given Open Amazon page
    When Amazon Shopping Cart Count has 0 items
    When Click on Shopping Cart icon
    Then Verify that user can see Amazon Cart is empty
