import jwt

from backend.security import JWT, Hasher
from backend.settings import settings


def test_verify_password_with_correct_password():
    pwd = 'test'
    hashed_pwd = Hasher.get_password_hash(pwd)

    assert Hasher.verify_password(pwd, hashed_pwd)


def test_verify_password_with_wrong_password():
    pwd = 'test'
    hashed_pwd = Hasher.get_password_hash(pwd)

    assert not Hasher.verify_password('wrong', hashed_pwd)


def test_encode_jwt():
    data = {'test': 'test'}
    token = JWT.encode(data)

    token = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert token['test'] == data['test']
    assert token['exp']


def test_decode_jwt():
    data = {'test': 'test'}
    token = JWT.encode(data)

    token = JWT.decode(token)

    assert token['test'] == data['test']
    assert token['exp']
