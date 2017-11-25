import string

def check_signup_pass(password):
    '''
    Password: String
    Function checks if password meets criteria:
        * Must be longer than 6 characters but smaller than 12
        * Must have 1 lowercase letter
        * Must have 1 uppercase letter
        * Must have 1 character
        * Must have 1 number
        * Cannot have any whitespace characters
    Returns Bool
    '''
    if len(password) < 6 or len(password) > 12:
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
    '''
    Username: String
    Function checks if username meets criteria:
        * Must be longer than 6 characters but smaller than 12
        * First character must be a letter
        * Can only have letters and numbers
    Returns Bool
    '''
    if len(username) < 6 or len(username) > 12:
        return False
    if not username[0].isalpha():
        return False
    for char in username:
        if char in string.whitespace or char in string.punctuation:
            return False
    return True