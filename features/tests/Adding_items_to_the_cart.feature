# Created by username at 6/27/20
Feature: Test Scenarios for Amazon Shopping Cart functionality

  Scenario: User can search for a product and successfully add it to the cart
    Given Open Amazon page
    When Input Mask into search field
    And Click on search icon
    Then Product results for Mask are shown
    And Click on first product in the search result
    And Click Add To Cart Button
    When Amazon Shopping Cart Count has 1 items
    And Click on Shopping Cart icon
    Then Verify that cart has 1 item