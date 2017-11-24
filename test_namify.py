from hash_password import make_hash_pass, check_hash_pass
from validate_signup import check_signup_pass
import pytest

passwords = ['python!M1', 'web@2B', 'cs14#S']

def test_make_hash():
    for password in passwords:
        assert type(make_hash_pass(password)) == str

def test_check_hash():
    hash_passwords = [make_hash_pass(password) for password in passwords]
    for password, hash_pass in zip(passwords, hash_passwords):
        assert check_hash_pass(password, hash_pass)

def test_check_signup_pass():
    for password in passwords:
        assert check_signup_pass(password)
    assert check_signup_pass('not valid') == False