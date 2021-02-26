from tests_for_todomvc.model import app_given, app_then, app_when


def test_create():
    app_given.visit()

    app_when.add()
    app_then.list_should_be_not()

    app_when.add('a', 'b')
    app_then.list_should_be('a', 'b')\
        .items_left_should_be(2)

    app_when.add('c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.follow_filter_active()
    app_then.list_should_be('a', 'b', 'c')

    app_when.follow_filter_completed()
    app_then.list_should_be_not()


def test_edit_by_enter():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.edit_by_enter('b', 'b edited')

    app_then.list_should_be('a', 'b edited', 'c')\
        .items_left_should_be(3)


def test_edit_by_focus_change():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.edit_by_tab('b', 'b edited')

    app_then.list_should_be('a', 'b edited', 'c')\
        .items_left_should_be(3)


def test_cancel_edit_by_escape():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.cancel_editing('b', 'b edited')

    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)


def test_complete():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.toggle('b')
    app_then.completed_todos_should_be('b')\
        .active_todos_should_be('a', 'c')\
        .items_left_should_be(2)\
        .clear_completed_visible()

    app_when.follow_filter_active()
    app_then.list_should_be('a', 'c')\
        .items_left_should_be(2)

    app_when.follow_filter_completed()
    app_then.list_should_be('b')\
        .items_left_should_be(2)


def test_complete_all():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.toggle_all()
    app_then.completed_todos_should_be('a', 'b', 'c')\
        .active_todos_should_be()\
        .items_left_should_be(0)\
        .clear_completed_visible()

    app_when.follow_filter_completed()
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(0)

    app_when.follow_filter_active()
    app_then.list_should_be_not()\
        .items_left_should_be(0)


def test_activate():
    app_given.visit()\
        .add('a', 'b', 'c')\
        .toggle_all()
    app_then.completed_todos_should_be('a', 'b', 'c')\
        .active_todos_should_be()\
        .items_left_should_be(0)\
        .clear_completed_visible()

    app_when.toggle('b')
    app_then.completed_todos_should_be('a', 'c')\
        .active_todos_should_be('b')\
        .items_left_should_be(1)

    app_when.toggle('a')\
        .toggle('c')
    app_then.active_todos_should_be('a', 'b', 'c')\
        .completed_todos_should_be()\
        .items_left_should_be(3)\
        .clear_completed_hidden()


def test_activate_all():
    app_given.visit()\
        .add('a', 'b', 'c')\
        .toggle_all()
    app_then.active_todos_should_be()\
        .completed_todos_should_be('a', 'b', 'c')\
        .items_left_should_be(0)\
        .clear_completed_visible()

    app_when.toggle_all()

    app_then.active_todos_should_be('a', 'b', 'c')\
        .completed_todos_should_be()\
        .items_left_should_be(3)\
        .clear_completed_hidden()


def test_delete_by_cross():
    app_given.visit()\
        .add('a', 'b', 'c')
    app_then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)

    app_when.delete('b')

    app_then.list_should_be('a', 'c')\
        .items_left_should_be(2)


def test_delete_by_edit():
    app_given.visit()\
        .add('a', 'b')
    app_then.list_should_be('a', 'b')\
        .items_left_should_be(2)

    app_when.edit_by_enter('a', '')
    app_then.list_should_be('b')\
        .items_left_should_be(1)

    app_when.edit_by_tab('b', '')
    app_then.list_should_be_not()\
        .footer_should_be_hidden()


def test_clear_completed():
    app_given.visit()\
        .add('a', 'b', 'c', 'd')
    app_then.list_should_be('a', 'b', 'c', 'd')\
        .items_left_should_be(4)
    app_given.toggle('b')\
        .toggle('d')

    app_when.clear_completed()
    app_then.list_should_be('a', 'c')\
        .items_left_should_be(2)\
        .clear_completed_hidden()

    app_when.follow_filter_active()
    app_then.list_should_be('a', 'c')

    app_when.follow_filter_completed()
    app_then.list_should_be_not()
