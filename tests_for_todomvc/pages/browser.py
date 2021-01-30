from selene import have
from selene.support.shared import browser


def open_application():
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.should(have.js_returned(True, "return $._data($("
                                          "'#clear-completed')[0],"
                                          "'events').hasOwnProperty("
                                          "'click')"))
    browser.config.set_value_by_js = True
