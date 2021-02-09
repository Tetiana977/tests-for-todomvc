from selene.support.shared import browser
from tests_for_todomvc.model import todomvc

browser.config.set_value_by_js = True


def test_create():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.add('c')
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(3)

    todomvc.follow_filter_active()
    todomvc.list_should_be('a', 'b', 'c')

    todomvc.follow_filter_completed()
    todomvc.list_should_be_not()


def test_edit_by_enter():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.edit_by_enter('a', 'a edited')
    todomvc.list_should_be('a edited', 'b')
    todomvc.items_left_should_be(2)


def test_edit_by_tab():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.edit_by_tab('a', 'a edited')
    todomvc.list_should_be('a edited', 'b')
    todomvc.items_left_should_be(2)


def test_edit_by_click_outside():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.edit_by_click_outside('a', 'a edited')
    todomvc.list_should_be('a edited', 'b')
    todomvc.items_left_should_be(2)


def test_cancel_edit_by_escape():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.cancel_editing('a', 'a edited')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)


def test_complete():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.toggle('a')
    todomvc.completed_todos_should_be('a')
    todomvc.active_todos_should_be('b')
    todomvc.items_left_should_be(1)

    todomvc.follow_filter_active()
    todomvc.list_should_be('b')
    todomvc.items_left_should_be(1)

    todomvc.follow_filter_completed()
    todomvc.list_should_be('a')
    todomvc.items_left_should_be(1)


def test_complete_all():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.toggle_all()
    todomvc.completed_todos_should_be('a', 'b')
    todomvc.items_left_should_be(0)

    todomvc.follow_filter_completed()
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(0)

    todomvc.follow_filter_active()
    todomvc.list_should_be_not()
    todomvc.items_left_should_be(0)


def test_activate():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.toggle('a')

    todomvc.toggle('a')
    todomvc.active_todos_should_be('a', 'b')
    todomvc.items_left_should_be(2)


def test_activate_all():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.toggle_all()

    todomvc.toggle_all()
    todomvc.active_todos_should_be('a', 'b')
    todomvc.items_left_should_be(2)


def test_delete_by_cross():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.delete('a')
    todomvc.list_should_be('b')
    todomvc.items_left_should_be(1)

    todomvc.follow_filter_active()
    todomvc.list_should_be('b')


def test_delete_by_edit():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')
    todomvc.list_should_be('a', 'b', 'c')
    todomvc.items_left_should_be(3)

    todomvc.edit_by_enter('a', '')
    todomvc.list_should_be('b', 'c')
    todomvc.items_left_should_be(2)

    todomvc.edit_by_enter('b', '')
    todomvc.list_should_be('c')
    todomvc.items_left_should_be(1)

    todomvc.edit_by_click_outside('c', '')
    todomvc.list_should_be_not()


def test_clear_completed():
    todomvc.visit()

    todomvc.add('a', 'b')
    todomvc.list_should_be('a', 'b')
    todomvc.items_left_should_be(2)

    todomvc.toggle('a')
    todomvc.clear_completed()
    todomvc.list_should_be('b')
    todomvc.items_left_should_be(1)

    todomvc.follow_filter_active()
    todomvc.list_should_be('b')

    todomvc.follow_filter_completed()
    todomvc.list_should_be_not()
