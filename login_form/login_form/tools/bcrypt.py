import bcrypt


def hash_password(password):
    # Genera un hash de la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def verify_password(password, hashed_password):
    # Verifica si la contraseña coincide con su hash almacenado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
