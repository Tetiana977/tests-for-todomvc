from tests_for_todomvc.pages import actions, browser


def test_todos_management():
    browser.open_application()

    actions.add('a', 'b', 'c')
    actions.list_should_be('a', 'b', 'c')

    actions.cancel_editing('c', 'c to be canceled')

    actions.delete('c')
    actions.list_should_be('a', 'b')

    actions.edit('a', 'a edited')

    actions.toggle('a edited')
    actions.clear_completed()
    actions.list_should_be('b')
