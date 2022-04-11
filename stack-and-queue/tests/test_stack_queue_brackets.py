from stack_and_queue.stack_queue_brackets import BracketValidation

def test_one_opening_one_closing():
    actual = BracketValidation.validate_brackets("{}")
    expected = True
    assert actual == expected

def test_multiple_openings_and_closing():
    actual = BracketValidation.validate_brackets("{}(){}")
    expected = True
    assert actual == expected

def test_multiple_nested_openings_and_closing():
    actual = BracketValidation.validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected

def test_missing_closing_bracket():
    actual = BracketValidation.validate_brackets("[({}]")
    expected = False
    assert actual == expected

def test_missing_closing_bracket_and_opening_bracket():
    actual = BracketValidation.validate_brackets("{(})")
    expected = False
    assert actual == expected

def test_nested_brackets_with_extra_char():
    actual = BracketValidation.validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_no_closing_brackets():
    actual = BracketValidation.validate_brackets("((")
    expected = False
    assert actual == expected

def test_no_opening_brackets():
    actual = BracketValidation.validate_brackets("]]")
    expected = False
    assert actual == expected