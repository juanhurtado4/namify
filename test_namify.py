from hash_password import make_hash_pass, check_hash_pass
from validate_signup import check_signup_pass, check_signup_username
import pytest

passwords = ['python!M1', 'web@2B', 'cs14#S']

def test_make_hash():
    '''Tests if password was hashed correctly'''
    for password in passwords:
        assert type(make_hash_pass(password)) == str

def test_check_hash():
    '''Tests if password is turned into hashed the same everytime'''
    hash_passwords = [make_hash_pass(password) for password in passwords]
    for password, hash_pass in zip(passwords, hash_passwords):
        assert check_hash_pass(password, hash_pass)

def test_check_signup_pass():
    '''Test if check_signup_pass function is catching passwords that do not meet criteria'''
    for password in passwords:
        assert check_signup_pass(password)
    assert check_signup_pass('not valid') == False
    assert check_signup_pass('notvalid') == False

def test_check_signup_username():
    '''Test if check_signup_username function is catching usernames that do not meet criteria'''    
    good_usernames = ['juanhurtado0', 'josemendes1', 'chris103']
    bad_usernames = ['usernametoolong', '3user', '123456', '123#!$juan', '!@@#$%^', 'juan hur']
    for username in good_usernames:
        assert check_signup_username(username)
    for username in bad_usernames:
        assert check_signup_username(username) == False