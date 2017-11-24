import hashlib

def make_hash_pass(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hash_pass(password, hash):
    if make_hash_pass(password) == has:
        return True
    
    return False