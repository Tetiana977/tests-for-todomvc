from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have

todos = ss('#todo-list>li')


def visit():
    download_page = "return $._data($('#clear-completed')[0]," \
                    "'events').hasOwnProperty('click')"

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


def edit_by_enter(name: str, new_text):
    start_editing(name, new_text).press_enter()


def edit_by_tab(name: str, new_text):
    start_editing(name, new_text).press_tab()


def edit_by_click_outside(name: str, new_text):
    start_editing(name, new_text)
    return s('footer').click()


def delete(name: str):
    todos.element_by(have.exact_text(name)).hover().element('.destroy').click()


def toggle(name: str):
    todos.element_by(have.exact_text(name)).element('.toggle').click()


def toggle_all():
    s('#toggle-all').click()


def clear_completed():
    s('#clear-completed').click()


def list_should_be(*names: str):
    todos.should(have.exact_texts(*names))


def items_left_should_be(amount: int):
    s('#todo-count strong').should(have.exact_text(str(amount)))


def follow_filter_active():
    s('#filters [href = "#/active"]').click()


def follow_filter_completed():
    s('#filters [href = "#/completed"]').click()


def list_should_be_not():
    todos.filtered_by(be.visible).should(have.size(0))


def completed_todos_should_be(*names: str):
    ss('#todo-list>li.completed').should(have.exact_texts(*names))


def active_todos_should_be(*names: str):
    ss('#todo-list>li:not(.completed)').should(have.exact_texts(*names))
