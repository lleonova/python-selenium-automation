# Created by username at 7/11/20
Feature: Test Scenarios for Amazon Blog link functionality

  Scenario: User can open and close Amazon Blog
    Given Open Amazon page
    When Store original windows
    And Click on blog link 'See daily updates at blog.aboutamazon.com'
    And Switch to the newly opened window
    Then Verify that Amazon Blog window is opened
    And User can open and close Blog menu
    And User can close new window and switch back to original