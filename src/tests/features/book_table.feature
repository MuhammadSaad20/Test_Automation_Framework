Feature: Verify Book Table Data

  Scenario: Verify that the data displayed in the Book Table matches the provided data sheet
    Given I navigate to the Pulp GUI book table page
    When I hover over the "Book" section in the header
    And I click on "Table" from the dropdown
    Then I should see the book table with the correct data
