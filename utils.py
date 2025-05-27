import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(hashed_password, input_password):
    return hashed_password == hashlib.sha256(input_password.encode()).hexdigest()
