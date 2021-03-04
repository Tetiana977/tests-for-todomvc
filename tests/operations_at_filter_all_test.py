from tests_for_todomvc.model import given, then, when


def test_create():
    given.visit()

    when.add()

    then.list_is_empty()

    when.add('a', 'b')

    then.list_is('a', 'b')\
        .items_left(2)

    when.add('c')

    then.list_is('a', 'b', 'c')\
        .items_left(3)


def test_edit_by_enter():
    given.visit_with('a', 'b', 'c')

    when.edit_by_enter('b', 'b edited')

    then.list_is('a', 'b edited', 'c')\
        .items_left(3)


def test_edit_by_focus_change():
    given.visit_with('a', 'b', 'c')

    when.edit_by_tab('b', 'b edited')

    then.list_is('a', 'b edited', 'c')\
        .items_left(3)


def test_cancel_edit_by_escape():
    given.visit_with('a', 'b', 'c')

    when.cancel_editing('b', 'b edited')

    then.list_is('a', 'b', 'c')\
        .items_left(3)


def test_complete():
    given.visit_with('a', 'b', 'c')

    when.toggle('b')

    then.completed_todos('b')\
        .active_todos('a', 'c')\
        .items_left(2)\
        .clear_completed_visible()


def test_complete_all():
    given.visit_with('a', 'b', 'c')\
        .toggle('b')

    when.toggle_all()

    then.completed_todos('a', 'b', 'c')\
        .active_todos()\
        .items_left(0)


def test_activate():
    given.visit_with('a', 'b', 'c')\
        .toggle_all()

    when.toggle('b')

    then.completed_todos('a', 'c')\
        .active_todos('b')\
        .items_left(1)

    when.toggle('a').toggle('c')

    then.active_todos('a', 'b', 'c')\
        .completed_todos()\
        .items_left(3)\
        .clear_completed_hidden()


def test_activate_all():
    given.visit_with('a', 'b', 'c')\
        .toggle_all()

    when.toggle_all()

    then.active_todos('a', 'b', 'c')\
        .completed_todos()\
        .items_left(3)\
        .clear_completed_hidden()


def test_delete():
    given.visit_with('a', 'b', 'c')

    when.delete('b')

    then.list_is('a', 'c')\
        .items_left(2)


def test_delete_by_edit():
    given.visit_with('a', 'b', 'c')

    when.edit_by_enter('a', '')

    then.list_is('b', 'c')\
        .items_left(2)

    when.edit_by_tab('b', '')

    then.list_is('c')\
        .items_left(1)


def test_clear_completed():
    given.visit().add('a', 'b', 'c', 'd')\
        .toggle('b').toggle('d')

    when.clear_completed()

    then.list_is('a', 'c')\
        .items_left(2)\
        .clear_completed_hidden()
