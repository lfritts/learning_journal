Feature: Show Select Edit Entries
    Add edit to each entry on the add entry screen.

    Scenario: Edit a post
        Given a post with id 1
        When I call edit_entry
        Then I see the edit entry screen for that entry

    Scenario: Submit an edit
        Given an edited post with id 1
        When I call submit_edit
        Then I see the updated entry