Feature: Line
    Represents either a row or a column in sudoku

Scenario: Allowed combinations of values
    Given I have a line
    And I populate the line with <values>
    When I validate the line
    Then The line should be valid

    Examples:
    | values            |
    | 0 0 0 0 0 0 0 0 0 |
    | 1 0 0 0 0 0 0 0 0 |
    | 1 2 0 0 0 0 0 0 0 |
    | 1 2 3 0 0 0 0 0 0 |
    | 1 2 3 4 0 0 0 0 0 |
    | 1 2 3 4 5 0 0 0 0 |
    | 1 2 3 4 5 6 0 0 0 |
    | 1 2 3 4 5 6 7 0 0 |
    | 1 2 3 4 5 6 7 8 0 |
    | 1 2 3 4 5 6 7 8 9 |

Scenario: Disallowed combinations of values
    Given I have a line
    And I populate the line with <values>
    When I validate the line
    Then The line should not be valid

    Examples:
    | values             |
    | 10 0 0 0 0 0 0 0 0 |
    | 1 1 0 0 0 0 0 0 0  |
    | 1 2 1 0 0 0 0 0 0  |
    | 1 2 13 0 0 0 0 0 0 |
    | 1 2 3 4 4 0 0 0 0  |
    | 1 2 3 4 5 2 0 0 0  |
    | 1 2 3 4 5 6 6 0 0  |
    | 1 2 3 4 5 6 1 0 0  |
    | 1 2 3 4 5 6 1 8 0  |
    | 1 2 3 4 5 6 1 8 9  |
