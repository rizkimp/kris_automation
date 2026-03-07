Feature: Login
  Scenario: User login with valid credentials
    Given user opens login page
    When user enters valid username and password
    And user clicks login button
    Then user should see dashboard