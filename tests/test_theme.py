
def test_theme():

    from ..src.themes import THEMES
    MUST_KEYS = [
        "background",

        "text_1",
        "text_2",
        "text_3",
        "text_4",

        "icons",
        "lines",
    ]
    for _, theme_data in THEMES.items():
        for key in MUST_KEYS:
            assert key in theme_data, "Theme data contains theme values"
