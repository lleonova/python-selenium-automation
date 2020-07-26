# Created by username at 6/22/20
Feature: Test Scenarios for Amazon Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Dress
    Then Product results for Dress are shown
#    And First result contains Computer


  Scenario: User can select Books department
    Given Open Amazon page
    When Select stripbooks department
    And Search for Faust
    Then Books department is selected


  Scenario: User can select Courses department
    Given Open Amazon page
    When Select courses department
    And Search for Python
    Then Courses department is selected