# Created by username at 7/3/20
Feature: Test Scenarios for Amazon WholeFoods Deals page functionality

  Scenario:  Every product on the page has a text ‘Regular’ and a product name
    Given Open Amazon WholeFoods Deals page
    Then Verify that every product on the page has a text Regular
    And Verify that every product on the page has a product name