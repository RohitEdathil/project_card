from ..src.formatters import format_number


def test_number_0_999():
    number = 999
    assert format_number(number) == str(
        number), 'Should return the same number if between (0 - 999)'


def test_number_char_small():
    number = 999
    assert format_number(number)[-1] == "9", 'Return the same number if small'


def test_number_char_K():
    number = 1000
    assert format_number(
        number)[-1] == "K", 'Return with K if (1000 - 999,999)'
    number = 999999
    assert format_number(
        number)[-1] == "K", 'Return with K if (1000 - 999,999)'


def test_number_char_M():
    number = 1000000
    assert format_number(
        number)[-1] == "M", 'Return with M if (1,000,000 - 999,999,999)'
    number = 999999999
    assert format_number(
        number)[-1] == "M", 'Return with M if (1,000,000 - 999,999,999)'


def test_number_char_B():
    number = 1000000000
    assert format_number(
        number)[-1] == "B", 'Return with B if (1,000,000,000 - 999,999,999,999)'
    number = 999999999999
    assert format_number(
        number)[-1] == "B", 'Return with B if (1,000,000,000 - 999,999,999,999)'


def test_number_char_T():
    number = 1000000000000
    assert format_number(
        number)[-1] == "T", 'Return with T if (1,000,000,000,000 - 999,999,999,999,999)'
    number = 999999999999999
    assert format_number(
        number)[-1] == "T", 'Return with T if (1,000,000,000,000 - 999,999,999,999,999)'


def test_number_char_Q():
    number = 1000000000000000
    assert format_number(
        number)[-1] == "Q", 'Return with Q if (1,000,000,000,000,000 - 999,999,999,999,999)'


def test_number_nums_small():
    number = 7000
    assert format_number(number) == "7K", 'Testing if n.n will appear'


def test_number_nums_small_decimal():
    number = 7100
    assert format_number(number) == "7.1K", 'Testing if n.n will appear'


def test_number_nums_medium():
    number = 70000
    assert format_number(number) == "70K", 'Testing if nn will appear'


def test_number_nums_large():
    number = 700000
    assert format_number(number) == "700K", 'Testing if nnn will appear'
