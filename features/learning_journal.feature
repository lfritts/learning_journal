Feature: Add ability to edit entries
    Add edit to each entry on the add entry screen.

    Scenario: Anonymous user can't see add entry form
        Given an anonymous user
        When I view the home page
        Then I do not see the new entry form

    Scenario: Logged in user can see add entry form
        Given an authenticated user
        When I view the home page
        Then I do see the new entry form

    Scenario: Anonymous user can't see edit entry link
        Given an anonymous user
        And any text
        And an existing entry
        When I view the home page
        Then I do not see the edit entry link

    Scenario: Logged in user can see edit entry link
        Given an authenticated user
        And any text
        And an existing entry
        When I view the home page
        Then I do see the edit entry link

    Scenario: Anonymous user can't see edit entry form
        Given an anonymous user
        When I add '/edit/1' to the home page url
        Then I do not see the edit entry form

    Scenario: Logged in user can see edit entry form
        Given an anonymous user
        When I add '/edit/1' to the home page url
        Then I do see the edit entry form

    Scenario: Anonymous user cannot submit add form
        Given an anonymous user
        And the title "New Post"
        And the text "This is a new post"
        When I submit the add form
        Then I am redirected to the home page
        And I do not see my new entry

    Scenario: Logged in user can submit add form
        Given an authenticated user
        And the title "New Post"
        And the text "This is a new post"
        When I submit the add form
        Then I am redirected to the home page
        And I see my new entry

    Scenario: Anonymous user cannot submit edit entry form
        Given an anonymous user
        And the title "Edited Post"
        And the text "This is an edited post"
        When I submit the edit form
        Then I am redirected to the home page
        And I do not see my new entry

    Scenario: Logged in user can submit edit entry form
        Given an authenticated user
        And the title "Edited Post"
        And the text "This is an edited post"
        When I submit the edit form
        Then I am redirected to the home page
        And I see my new entry

    Scenario: Users can see colorized code samples
        Given text containing markdown and plain text
        And an existing entry
        When I view the home page
        Then I see code highlighted in color
        And I see plain text without color
