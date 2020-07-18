# Created by username at 7/17/20
Feature: Test for Hamburger Menu functionality

   Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present