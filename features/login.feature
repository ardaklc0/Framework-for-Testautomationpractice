Feature: Field Filling
  As a user
  I want to fill fields in the Automation Testing Practice application

  Scenario: Filling fields with valid credentials
    Given Automation Testing Practice page is displayed
    When the user enters valid credentials
    Then the home page should be displayed