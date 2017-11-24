from hash_password import make_hash_pass, check_hash_pass
import pytest

def test_make_hash():
    password1 = 'python'
    password2 = 'javascript'
    password3 = 'computer_science'
    assert type(make_hash_pass(password1)) == str
    assert type(make_hash_pass(password2)) == str
    assert type(make_hash_pass(password3)) == str