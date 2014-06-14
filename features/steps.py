from lettuce import step
from lettuce import world
from learning_journal import app


@step('the displayed entries with an edit button (\d+)')
def the_entry_id(step, num):
    world.number = int(num)


@step('when I click edit')
def call_edit_screen_template(step):
    world.edit = app.edit_entry(world.number)


@step('I see the edit screen')
def show_entry(step, expected):
    assert world.edit == expected, "Got %d" % expected
