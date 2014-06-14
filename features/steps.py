from lettuce import step
from lettuce import world
from journal import app


@step('a post with id (\d+)')
def the_entry_id(step, num):
    world.number = int(num)


@step('when I click edit')
def call_edit_screen_template(step):
    world.edit = app.edit_entry(world.number)


@step('I see the edit screen')
def show_entry(step, expected):
    assert world.edit == expected, "Got %d" % expected


@step('an edited post with id (\d+)')
def the_edited_post(step, num):
    world.number = int(num)


@step('when I click submit')
def call_update(step):
    world.update = app.update_entry(world.number)


@step('I see the updated post')
def something(step, expected):
    assert world.update == expected, "Got %d" % expected
