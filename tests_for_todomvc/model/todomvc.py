from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have

todos = ss('#todo-list>li')


class TodoMvcPage:

    def visit(self):
        download_page = "return $._data($('#clear-completed')[0]," \
                        "'events').hasOwnProperty('click')"

        browser.open('https://todomvc4tasj.herokuapp.com')
        browser.should(have.js_returned(True, download_page))
        return self

    def add(self, *names: str):
        for name in names:
            s('#new-todo').type(name).press_enter()
        return self

    def start_editing(self, name: str, new_text):
        todos.element_by(have.exact_text(name)).double_click()
        return todos.element_by(have.css_class('editing')) \
            .element('.edit').set_value(new_text)

    def cancel_editing(self, name: str, new_text):
        self.start_editing(name, new_text).press_escape()
        return self

    def edit_by_enter(self, name: str, new_text):
        self.start_editing(name, new_text).press_enter()
        return self

    def edit_by_tab(self, name: str, new_text):
        self.start_editing(name, new_text).press_tab()
        return self

    def edit_by_click_outside(self, name: str, new_text):
        self.start_editing(name, new_text)
        return s('footer').click()

    def delete(self, name: str):
        todos.element_by(have.exact_text(name)).hover() \
            .element('.destroy').click()
        return self

    def toggle(self, name: str):
        todos.element_by(have.exact_text(name)).element('.toggle').click()
        return self

    def toggle_all(self):
        s('#toggle-all').click()
        return self

    def clear_completed(self):
        s('#clear-completed').click()
        return self

    def list_should_be(self, *names: str):
        todos.should(have.exact_texts(*names))
        return self

    def items_left_should_be(self, amount: int):
        s('#todo-count strong').should(have.exact_text(str(amount)))
        return self

    def follow_filter_active(self):
        s('#filters [href = "#/active"]').click()
        return self

    def follow_filter_completed(self):
        s('#filters [href = "#/completed"]').click()
        return self

    def list_should_be_not(self):
        todos.filtered_by(be.visible).should(have.size(0))
        return self

    def completed_todos_should_be(self, *names: str):
        ss('#todo-list>li.completed').should(have.exact_texts(*names))
        return self

    def active_todos_should_be(self, *names: str):
        ss('#todo-list>li:not(.completed)').should(have.exact_texts(
            *names))
        return self
