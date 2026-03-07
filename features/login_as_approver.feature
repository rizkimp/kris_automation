Feature: login as approver
  Scenario: User login as approver with valid credentials
    Given user opens login page
    When user enters valid username and password as approver
    And user clicks login button
    Then user should see dashboard