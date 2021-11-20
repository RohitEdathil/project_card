from ..src.formatters import format_file


def test_file_B():
    n = 300
    assert format_file(n) == "300B", 'Should return file size as B'


def test_file_KB():
    n = 3000
    assert format_file(n) == "3KB", 'Should return file size as KB'


def test_file_MB():
    n = 3000000
    assert format_file(n) == "3MB", 'Should return file size as MB'


def test_file_GB():
    n = 3000000000
    assert format_file(n) == "3GB", 'Should return file size as GB'


def test_file_TB():
    n = 3000000000000
    assert format_file(n) == "3TB", 'Should return file size as GB'
