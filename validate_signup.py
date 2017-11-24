import string

# TODO: Finish logic for check_signup_username function

def check_signup_pass(password):
    if len(password)<6 or len(password)>12:
        return False
    counter = {'lower': 0, 'upper': 0, 'char': 0, 'digit': 0}
    for char in password:
        if char in string.ascii_lowercase:
            counter['lower'] = 1
        elif char in string.ascii_uppercase:
            counter['upper'] = 1
        elif char in string.punctuation:
            counter['char'] = 1
        elif char in string.digits:
            counter['digit'] = 1
        elif char in string.whitespace:
            return False
    if sum(counter.values()) >= 4:
        return True
    return False

def check_signup_username(username):
    pass