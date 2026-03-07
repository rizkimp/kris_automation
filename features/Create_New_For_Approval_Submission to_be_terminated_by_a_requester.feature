Feature: Create New “For Approval” Submission to be terminated by a requester
    Scenario: Create New “For Approval” Submission to be terminated by a requester
        Given user is on the "E-submission" module
        When user clicks "New Submission" and selects "For Approval"
        And user fills all mandatory fields with valid data
        And user uploads a valid pdf file as the main paper
        And user uploads at least one attachment file
        And user adds at least one folder from the "Recent" tab
        And user adds "t2user5" as the action officer in routing type
        And user clicks the "Submit" button
        And user confirms the submission in the confirmation popup
        Then the submission should be created successfully
        When user clicks the "Terminate" button
        And user enters a valid termination reason
        And user confirms the termination
        Then the submission should be terminated successfully