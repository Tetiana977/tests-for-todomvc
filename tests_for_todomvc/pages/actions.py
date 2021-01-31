from selene import have
from selene.support.shared.jquery_style import s, ss

todos = ss('#todo-list>li')


def add(*names):
    for name in names:
        s('#new-todo').type(name).press_enter()


def start_editing(name, new_text):
    todos.element_by(have.exact_text(name)).double_click()
    return todos.element_by(have.css_class('editing')).element('.edit') \
        .set_value(new_text)


def cancel_editing(name, new_text):
    start_editing(name, new_text).press_escape()


def edit(name, new_text):
    start_editing(name, new_text).press_enter()


def delete(name):
    todos.element_by(have.exact_text(name)).element('.destroy').click()


def toggle(name):
    todos.element_by(have.exact_text(name)).element('.toggle').click()


def clear_completed():
    s('#clear-completed').click()


def list_should_be(*names: str):
    todos.should(have.exact_texts(*names))
