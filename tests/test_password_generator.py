from practice.password_generator import generate_password

def test_generate_default_password():
    p = generate_password()
    assert isinstance(p, str)
    assert len(p) >= 8

def test_generate_custom_length_and_chars():
    p = generate_password(length=16, use_numbers=False, use_symbols=False)
    assert len(p) == 16
