from tests_for_todomvc.model import app_given, app_then, app_when


def test_todos_management():

    app_given.visit()

    app_when.add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')

    app_when.cancel_editing('c', 'c to be canceled')

    app_when.delete('c')
    app_then.list_should_be('a', 'b')

    app_when.edit_by_tab('a', 'a edited')

    app_when.toggle('a edited')
    app_when.clear_completed()
    app_then.list_should_be('b')
