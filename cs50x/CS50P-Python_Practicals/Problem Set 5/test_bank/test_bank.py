import bank


def test_value_hello():
    greeting = "Hello, world!"
    expected_output = 0
    assert bank.value(greeting) == expected_output


def test_value_h():
    greeting = "Hey there!"
    expected_output = 20
    assert bank.value(greeting) == expected_output


def test_value_default():
    greeting = "Hi!"
    expected_output = 20
    assert bank.value(greeting) == expected_output


def test_value_case_insensitive():
    greeting = "hELlo, FrIeNd!"
    expected_output = 0
    assert bank.value(greeting) == expected_output


def test_value_entire_phrase():
    greeting = "Hello there, how are you?"
    expected_output = 0
    assert bank.value(greeting) == expected_output
