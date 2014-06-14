Feature: Show Select Edit Entries
    Add edit to each entry on the add entry screen.

    Scenario:  Select an entry for editing
        Given the displayed entries with an edit button
        When I click the edit button of an entry
        Then I see the edit entry screen for that entry