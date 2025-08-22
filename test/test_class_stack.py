import pytest
import main

@pytest.fixture
def stack():
    return main.Stack()


def test_stack_is_empty(stack):

    expected = 0

    res = stack.count

    assert expected == res, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_in_stack_1(stack):

    expected = 1

    stack.push(5)

    res = stack.count

    assert expected == res, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_in_stack_2(stack):

    expected = 3

    stack.push(5), stack.push(1), stack.push(13)

    res = stack.count

    assert expected == res, f'Ожидали:{expected}, получили:{res}'


def test_peek_elem_from_stack(stack):

    expected = 13

    stack.push(5), stack.push(1), stack.push(13)

    res = stack.peek()

    assert expected == res, f'Ожидали:{expected}, получили:{res}'


def test_pop_elem_from_stack_1(stack):

    expected_1 = 13
    expected_2 = 2

    stack.push(5), stack.push(1), stack.push(13)

    res_1 = stack.pop()
    res_2 = stack.count

    assert expected_1 == res_1, f'Ожидали:{expected_1}, получили:{res_1}'
    assert expected_2 == res_2, f'Ожидали:{expected_2}, получили:{res_2}'


def test_pop_elem_from_stack_2(stack):

    expected_1 = 5
    expected_2 = 0

    stack.push(5), stack.push(1), stack.push(13)

    stack.pop(), stack.pop()
    res_1 = stack.pop()
    res_2 = stack.count

    assert expected_1 == res_1, f'Ожидали:{expected_1}, получили:{res_1}'
    assert expected_2 == res_2, f'Ожидали:{expected_2}, получили:{res_2}'
