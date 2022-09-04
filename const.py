import jwt

algorithm_H = "HS256"


def encoded_information(json, key, algorithm=algorithm_H):
    return jwt.encode(json, key, algorithm=algorithm)


def decoded_information(encoded, key, algorithm=algorithm_H):
    return jwt.decode(encoded, key, algorithms=algorithm)
