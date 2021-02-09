from selene.support.shared import browser
from tests_for_todomvc.model import todomvc


def test_todos_management():
    browser.config.set_value_by_js = True

    todomvc.visit()

    todomvc.add('a', 'b', 'c')
    todomvc.list_should_be('a', 'b', 'c')

    todomvc.cancel_editing('c', 'c to be canceled')

    todomvc.delete('c')
    todomvc.list_should_be('a', 'b')

    todomvc.edit_by_tab('a', 'a edited')

    todomvc.toggle('a edited')
    todomvc.clear_completed()
    todomvc.list_should_be('b')
