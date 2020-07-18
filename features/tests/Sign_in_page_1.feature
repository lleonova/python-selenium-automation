# Created by username at 6/25/20
Feature: Test Scenarios for Amazon Sign In functionality

  Scenario: Logged out user can see Sign in page when clicking Orders
    Given Open Amazon Help page
    When Click Returns And Orders
    Then Verify Sign In page is opened
