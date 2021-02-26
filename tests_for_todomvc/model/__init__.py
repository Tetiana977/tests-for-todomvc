from tests_for_todomvc.model.todomvc import TodoMvcPrecondition, \
    TodoMvcAssert, TodoMvcAct

app_given = TodoMvcPrecondition()
app_when = TodoMvcAct()
app_then = TodoMvcAssert()
