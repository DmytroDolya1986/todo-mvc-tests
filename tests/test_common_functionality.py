from todo_mvc_tests.model import todomvc


def test_primal_app_functionality():
    todomvc.given_opened_with()

    todomvc.create('a', 'b', 'c')

    todomvc.should_have('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.toggle('b edited')

    todomvc.clear_completed()
    todomvc.should_have('a', 'c')

    todomvc.cancel_editing('c', 'to be canceled')

    todomvc.delete('c')
    todomvc.should_have('a')
