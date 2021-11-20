from ..src.formatters import *


# Description tests
def test_desc_small():
    desc = 'Short description'
    assert format_desc(desc) == (
        desc, '', ''), 'Should return the same description if small'


def test_desc_medium():
    desc = "a"*35 + "b"*10
    assert format_desc(desc) == (
        "a"*35, "b"*10, ''), 'Splits into two if medium size'


def test_desc_large():
    desc = "a"*35 + "b"*35 + "c"*10
    assert format_desc(desc) == (
        "a"*35, "b"*35, "c"*10), 'Splits into three if large size'


def test_desc_very_large():
    desc = "a"*35 + "b"*35 + "c"*35 + "d"*10
    assert format_desc(desc) == (
        "a"*35, "b"*35, "c"*32 + "..."), 'Splits into three and adds ... if very large'

# Title tests


def test_title_small():
    title = "Hello"
    assert format_title(
        title) == title, 'Should return the same title if small'


def test_title_large():
    title = "a"*20
    assert format_title(
        title) == "a"*13 + '...', 'Should return trencated'

# Date tests


def test_date():
    date = "2021-09-14T15:17:43Z"
    assert format_date(
        date) == "2021-09-14 15:17:43", 'Removes T and Z'

# Title tests


def test_title_small():
    title = "Hello"
    assert format_title(
        title) == title, 'Should return the same license'


def test_title_large():
    title = "a"*25
    assert format_title(
        title) == "a"*13 + '...', 'Should return truncated'
