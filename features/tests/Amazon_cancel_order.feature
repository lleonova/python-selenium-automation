# Created by username at 6/24/20
Feature: Test Scenarios for Help Search functionality
  # Enter feature description here

  Scenario: Verify user can search for info on how to cancel order
    Given Open Amazon Help page
    When Input Cancel order into Help search field
    And Click on Help search icon
    Then Product results for Help Cancel Items or Orders are shown
