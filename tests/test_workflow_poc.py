from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_todos_management():
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
    ss('#todo-list>li').should(have.exact_texts('b'))
