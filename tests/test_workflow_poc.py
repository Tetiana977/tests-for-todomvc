from selene.support.shared import browser
from tests_for_todomvc.pages import actions, browser


'''def test_todos_management():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, "return $._data($("
                                          "'#clear-completed')[0],"
                                          "'events').hasOwnProperty("
                                          "'click')"))
    browser.config.set_value_by_js = True

    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()
    ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    ss('#todo-list>li').element_by(have.exact_text('c')).double_click()
    ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
        .set_value('c to be canceled').press_escape()

    ss('#todo-list>li').element_by(have.exact_text('c')).element('.destroy')\
        .click()
    ss('#todo-list>li').should(have.exact_texts('a', 'b'))

    ss('#todo-list>li').element_by(have.exact_text('a')).double_click()
    ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
        .set_value('a edited').press_enter()

    ss('#todo-list>li').element_by(have.exact_text('a edited'))\
        .element('.toggle').click()
    s('#clear-completed').click()
    ss('#todo-list>li').should(have.exact_texts('b'))'''


def test_todos_management_refactor():
    browser.open_application()

    actions.add('a')
    actions.add('b')
    actions.add('c')
    actions.should_be_text('a', 'b', 'c')

    actions.cancel_editing('c', 'c to be canceled')

    actions.delete('c')
    actions.should_be_text('a', 'b')

    actions.edit('a', 'a edited')

    actions.completed('a edited')
    actions.clear_completed()
    actions.should_be_text('b')
