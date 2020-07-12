# Created by username at 7/10/20
Feature: Test Scenarios for Amazon Best Sellers Links functionality

  Scenario: Click on each Amazon BestsSellers link opens up a correct page
    Given Open Amazon page
    Then Click on BestSellers icon
    And Verify that each Top Menu link opens up a corresponding page