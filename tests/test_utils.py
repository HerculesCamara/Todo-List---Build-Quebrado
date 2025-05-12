from app.utils import format_title

def test_format_title():
    assert format_title("  ola mundo ") == "Ola mundo"
