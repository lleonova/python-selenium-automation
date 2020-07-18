# Created by username at 7/17/20
Feature: Test Scenarios for Amazon Sign In Page functionality

  Scenario: Logged out user can see Sign in page when clicking Orders
    Given Open Amazon page
    When Click on the Returns And Orders link
    Then Verify Sign In page is opened
