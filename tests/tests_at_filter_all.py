from selene.support.shared import browser
from tests_for_todomvc.model.todomvc import TodoMvcPage

browser.config.set_value_by_js = True


def test_create():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().add('c')
    TodoMvcPage().list_should_be('a', 'b', 'c')
    TodoMvcPage().items_left_should_be(3)

    TodoMvcPage().follow_filter_active()
    TodoMvcPage().list_should_be('a', 'b', 'c')

    TodoMvcPage().follow_filter_completed()
    TodoMvcPage().list_should_be_not()


def test_edit_by_enter():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().edit_by_enter('a', 'a edited')
    TodoMvcPage().list_should_be('a edited', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_edit_by_tab():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().edit_by_tab('a', 'a edited')
    TodoMvcPage().list_should_be('a edited', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_edit_by_click_outside():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().edit_by_click_outside('a', 'a edited')
    TodoMvcPage().list_should_be('a edited', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_cancel_edit_by_escape():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().cancel_editing('a', 'a edited')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_complete():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().toggle('a')
    TodoMvcPage().completed_todos_should_be('a')
    TodoMvcPage().active_todos_should_be('b')
    TodoMvcPage().items_left_should_be(1)

    TodoMvcPage().follow_filter_active()
    TodoMvcPage().list_should_be('b')
    TodoMvcPage().items_left_should_be(1)

    TodoMvcPage().follow_filter_completed()
    TodoMvcPage().list_should_be('a')
    TodoMvcPage().items_left_should_be(1)


def test_complete_all():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().toggle_all()
    TodoMvcPage().completed_todos_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(0)

    TodoMvcPage().follow_filter_completed()
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(0)

    TodoMvcPage().follow_filter_active()
    TodoMvcPage().list_should_be_not()
    TodoMvcPage().items_left_should_be(0)


def test_activate():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().toggle('a')

    TodoMvcPage().toggle('a')
    TodoMvcPage().active_todos_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_activate_all():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().toggle_all()

    TodoMvcPage().toggle_all()
    TodoMvcPage().active_todos_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)


def test_delete_by_cross():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().delete('a')
    TodoMvcPage().list_should_be('b')
    TodoMvcPage().items_left_should_be(1)

    TodoMvcPage().follow_filter_active()
    TodoMvcPage().list_should_be('b')


def test_delete_by_edit():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b', 'c')
    TodoMvcPage().list_should_be('a', 'b', 'c')
    TodoMvcPage().items_left_should_be(3)

    TodoMvcPage().edit_by_enter('a', '')
    TodoMvcPage().list_should_be('b', 'c')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().edit_by_enter('b', '')
    TodoMvcPage().list_should_be('c')
    TodoMvcPage().items_left_should_be(1)

    TodoMvcPage().edit_by_click_outside('c', '')
    TodoMvcPage().list_should_be_not()


def test_clear_completed():
    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b')
    TodoMvcPage().list_should_be('a', 'b')
    TodoMvcPage().items_left_should_be(2)

    TodoMvcPage().toggle('a')
    TodoMvcPage().clear_completed()
    TodoMvcPage().list_should_be('b')
    TodoMvcPage().items_left_should_be(1)

    TodoMvcPage().follow_filter_active()
    TodoMvcPage().list_should_be('b')

    TodoMvcPage().follow_filter_completed()
    TodoMvcPage().list_should_be_not()
