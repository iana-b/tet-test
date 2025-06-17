import pytest
from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def create_user(first_name: str, last_name: str, age: int) -> str:
    return f"{first_name} {last_name}, {age}"


@strict
def expect_bool(flag: bool) -> str:
    return f"Flag is {flag}"


def test_sum_two_success():
    assert sum_two(1, 2) == 3


def test_sum_two_type_error():
    with pytest.raises(TypeError) as exc:
        sum_two(1, 2.4)
    assert "Expected int, got float" in str(exc.value)


def test_sum_two_missing_arg():
    with pytest.raises(TypeError) as exc:
        sum_two(1)
    assert "Incorrect number of arguments" in str(exc.value)


def test_sum_two_too_many_args():
    with pytest.raises(TypeError) as exc:
        sum_two(1, 2, 3)
    assert "Incorrect number of arguments" in str(exc.value)


def test_create_user_success():
    result = create_user("Jane", "Doe", 30)
    assert result == "Jane Doe, 30"


def test_create_user_wrong_type():
    with pytest.raises(TypeError) as exc:
        create_user("John", "Doe", "thirty")
    assert "Expected int, got str" in str(exc.value)


def test_expect_bool_true():
    assert expect_bool(True) == "Flag is True"


def test_expect_bool_false():
    assert expect_bool(False) == "Flag is False"


def test_expect_bool_int():
    with pytest.raises(TypeError) as exc:
        expect_bool(1)
    assert "Expected bool, got int" in str(exc.value)
