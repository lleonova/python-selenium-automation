# Created by username at 7/25/20
Feature: Test scenarios for Amazon Fashion Product functionality

  Scenario: When hovering over New Arrivals user can see the deals
    Given Open Amazon B074TBCSC8 product page
    When Hovering over New Arrivals
    Then Verify the user sees the deals