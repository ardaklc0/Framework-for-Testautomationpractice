Feature: Login and Logout
  As a user
  I want to login and logout of the Automation Testing Practice application

  Scenario: Valid Login
    Given Automation Testing Practice page is displayed
    When the user enters valid credentials
    Then the home page should be displayed