from greet import greet


def test_greet_with_name():
    assert greet("world") == "Hello, world!"


def test_greet_without_name():
    assert greet("") == "Hello, stranger!"
