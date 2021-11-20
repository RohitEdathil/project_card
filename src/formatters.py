
from typing import Tuple


def format_title(title: str) -> str:
    """
    Formats the title of a project.
    """
    MAX = 16
    if len(title) > MAX:
        title = title[:MAX-3] + '...'
    return title


def format_desc(desc: str) -> Tuple[str, str, str]:
    """
    Formats the description of a project.
    """
    MAX = 35
    desc1, desc2, desc3 = desc, '', ''

    if len(desc) > MAX:
        desc2 = desc1[MAX:]
        desc1 = desc1[:MAX]
    if len(desc2) > MAX:
        desc3 = desc2[MAX:]
        desc2 = desc2[:MAX]
    if len(desc3) > MAX:
        desc3 = desc3[:MAX-3] + '...'
    return desc1, desc2, desc3


def format_number(n: int) -> str:
    """
    Formats large numbers using K M B T Q
    """

    if n < 1000:
        return str(n)

    if n < 10000:
        s = str(f"{n/1000:.1f}")
        if s[-1] == '0':
            return s[:-2] + "K"
        return s + "K"
    if n < 1000000:
        return str(f"{n/1000:.0f}K")

    if n < 10000000:
        s = str(f"{n/1000**2:.1f}")
        if s[-1] == '0':
            return s[:-2] + "M"
        return s + "M"
    if n < 1000000000:
        return str(f"{n/1000**2:.0f}M")

    if n < 10000000000:
        s = str(f"{n/1000**3:.1f}")
        if s[-1] == '0':
            return s[:-2] + "B"
        return s + "B"
    if n < 1000000000000:
        return str(f"{n/1000**3:.0f}B")

    if n < 10000000000000:
        s = str(f"{n/1000**4:.1f}")
        if s[-1] == '0':
            return s[:-2] + "T"
        return s + "T"
    if n < 1000000000000000:
        return str(f"{n/1000**4:.0f}T")

    return str(f"{n/1000**5:.0f}Q")


def format_file(num: int) -> str:
    """
    Format sizes using KB MB GB TB
    """
    suffix = "B"
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:.0f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def format_date(date: str) -> str:
    """
    Format dates using YYYY-MM-DD HH:MM:SS
    """
    return date.replace('T', ' ').replace('Z', '')


def format_license(license: str) -> str:
    """
    Format license using a short name
    """
    MAX = 21
    if len(license) > MAX:
        license = license[:MAX-3] + '...'
    return license
