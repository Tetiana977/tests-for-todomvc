from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have

todos = ss('#todo-list>li')
download_page = "return $._data($('#clear-completed')[0]," \
              "'events').hasOwnProperty('click')"


def visit():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, download_page))


def add(*names: str):
    for name in names:
        s('#new-todo').type(name).press_enter()


def start_editing(name: str, new_text):
    todos.element_by(have.exact_text(name)).double_click()
    return todos.element_by(have.css_class('editing')).element('.edit') \
        .set_value(new_text)


def cancel_editing(name: str, new_text):
    start_editing(name, new_text).press_escape()


def edit(name: str, new_text):
    start_editing(name, new_text).press_enter()


def delete(name: str):
    todos.element_by(have.exact_text(name)).element('.destroy').click()


def toggle(name: str):
    todos.element_by(have.exact_text(name)).element('.toggle').click()


def clear_completed():
    s('#clear-completed').click()


def list_should_be(*names: str):
    todos.should(have.exact_texts(*names))
