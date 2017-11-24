from hash_password import make_hash_pass, check_hash_pass
import pytest

passwords = ['python', 'javascript', 'computer_science']

def test_make_hash():
    for password in passwords:
        assert type(make_hash_pass(password)) == str

def test_check_hash():
    hash_passwords = [make_hash_pass(password) for password in passwords]
    for password, hash_pass in zip(passwords, hash_passwords):
        assert check_hash_pass(password, hash_pass)
