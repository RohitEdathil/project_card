
from typing import Tuple


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


def format_title(title: str) -> str:
    """
    Formats the title of a project.
    """
    MAX = 16
    if len(title) > MAX:
        title = title[:MAX-3] + '...'
    return title
