from selene import have
from selene.support.shared.jquery_style import s, ss

todos = ss('#todo-list>li')
edit_field = todos.element_by(have.css_class('editing')).element('.edit')


def add(text: str):
    s('#new-todo').type(text).press_enter()


def cancel_editing(text: str, new_text: str):
    todos.element_by(have.exact_text(text)).double_click()
    return edit_field.set_value(new_text).press_escape()


def edit(text: str, new_text: str):
    todos.element_by(have.exact_text(text)).double_click()
    return edit_field.set_value(new_text).press_enter()


def delete(text: str):
    todos.element_by(have.exact_text(text)).element('.destroy') \
        .click()


def completed(text: str):
    todos.element_by(have.exact_text(text)) \
        .element('.toggle').click()


def clear_completed():
    s('#clear-completed').click()


def should_be_text(*args: str):
    todos.should(have.exact_texts(*args))
