import lettuce

from flask import url_for
from journal import app
from journal import init_db
from test_journal import clear_db
from test_journal import TEST_DSN


@lettuce.before.all
def setup_app():
    app.config['DATABASE'] = TEST_DSN
    app.config['TESTING'] = True
    init_db()


@lettuce.after.all
def teardown_app(total):
    clear_db()


@lettuce.step('an anonymous user')
def anonymous_user(step):
    with app.test_client() as client:
        lettuce.world.client = client


@lettuce.step('an authenticated user')
def authenticated_user(step):
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['logged_in'] = True
        lettuce.world.client = client


@lettuce.step('I view the home page')
def request_homepage(step):
    with app.test_request_context('/'):
        home_url = url_for('show_entries')
    lettuce.world.response = lettuce.world.client.get(home_url)


@lettuce.step('I do not see the new entry form')
def no_entry_form(step):
    body = lettuce.world.response.data
    msg = 'found add_entry form in %s'
    assert 'class="add_entry"' not in body, msg % body


@lettuce.step('I do see the new entry form')
def yes_entry_form(step):
    body = lettuce.world.response.data
    msg = "did not find 'add_entry' form in %s"
    assert 'class="add_entry"' in body, msg % body


@lettuce.step("I add '/edit/1' to the home page url")
def anonymous_request_edit_page(step):
    with app.test_request_context('/'):
        edit_url = url_for('show_entries') + "edit/1"
    lettuce.world.response = lettuce.world.client.get(edit_url)


@lettuce.step('I do not see the edit entry form')
def no_edit_entry_form(step):
    body = lettuce.world.response.data
    msg = 'found value="Accept" in %s'
    assert 'value="Accept"' not in body, msg % body


@lettuce.step('I do see the edit entry form')
def yes_edit_entry_form(step):
    body = lettuce.world.response.data
    msg = 'did not find value="Accept" in %s'
    assert 'value="Accept"' in body, msg % body


@lettuce.step('the title "([^"]*)"')
def title_input(step, title):
    lettuce.world.title = title


@lettuce.step('the text "([^"]*)"')
def text_input(step, text):
    lettuce.world.text = text


@lettuce.step('I submit the add form')
def add_entry(step):
    entry_data = {
        'title': lettuce.world.title,
        'text': lettuce.world.text,
    }
    lettuce.world.response = lettuce.world.client.post(
        '/add', data=entry_data, follow_redirects=False
    )


@lettuce.step('I submit the edit form')
def edit_entry(step):
    entry_data = {
        'title': 'Some new title',
        'text': 'Some new text',
    }
    lettuce.world.response = lettuce.world.client.post(
        '/update_entry/1', data=entry_data, follow_redirects=False
    )


@lettuce.step('I am redirected to the home page')
def redirected_home(step):
    with app.test_request_context('/'):
        home_url = url_for('show_entries')
    # assert that we have been redirected to the home page
    assert lettuce.world.response.status_code in [301, 302]
    assert lettuce.world.response.location == 'http://localhost' + home_url
    # now, fetch the homepage so we can finish this off.
    lettuce.world.response = lettuce.world.client.get(home_url)


@lettuce.step('I do not see my new entry')
def no_new_entry(step):
    body = lettuce.world.response.data
    for val in [lettuce.world.title, lettuce.world.text]:
        assert val not in body, body


@lettuce.step('I see my new entry')
def yes_new_entry(step):
    body = lettuce.world.response.data
    print body
    for val in [lettuce.world.title, lettuce.world.text]:
        assert val in body


@lettuce.step('I see my edited entry')
def yes_new_entry(step):
    body = lettuce.world.response.data
    print body
    assert '<h3>Some new title</h3>' in body
    assert '<p>Some new text</p>' in body


@lettuce.step('any text')
def random_text(step):
    lettuce.world.text = "This is sample text."


@lettuce.step('an existing entry')
def existing_entry(step):
    lettuce.world.title = "My Title"
    entry_data = {
        'title': lettuce.world.title,
        'text': lettuce.world.text,
    }
    lettuce.world.response = lettuce.world.client.post(
        '/add', data=entry_data, follow_redirects=False
    )


@lettuce.step('Then I do not see the edit entry link')
def no_edit_link(step):
    body = lettuce.world.response.data
    msg = "found edit link in %s"
    assert 'a href="edit"' not in body, msg % body


@lettuce.step('Then I do see the edit entry link')
def yes_edit_link(step):
    body = lettuce.world.response.data
    msg = "did not find edit link in %s"
    assert 'a href="edit/1"' in body, msg % body


@lettuce.step('text containing markdown and plain text')
def text_with_markdown_and_plain(step):
    lettuce.world.text = \
        'Sample plain text.\n\n     `code samples`'


@lettuce.step('I see code highlighted in color')
def see_highlighted_code(step):
    body = lettuce.world.response.data
    msg = 'did not find <div class="codehilite"> in %s'
    assert '<div class="codehilite">' in body, msg % body


@lettuce.step('I see plain text without color')
def see_plain_text(step):
    body = "".join(lettuce.world.response.data.split())
    msg1 = 'did not find <divclass="entry_body"><p>Sampleplaintext.</p> in %s'
    assert '<divclass="entry_body"><p>Sampleplaintext.</p>' in \
        body, msg1 % body
    msg2 = 'found <divclass="codehilite"><p>Sampleplaintext.</p> in %s'
    assert '<divclass="codehilite"><p>Sampleplaintext.</p>' not in \
        body, msg2 % body
