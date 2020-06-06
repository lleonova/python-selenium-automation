# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Computer into search field
    And Click on search icon
    Then Product results for Computer are shown
    And First result contains Computer