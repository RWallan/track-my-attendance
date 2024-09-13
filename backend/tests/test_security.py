from backend.security import Hasher


def test_verify_password_with_correct_password():
    pwd = 'test'
    hashed_pwd = Hasher.get_password_hash(pwd)

    assert Hasher.verify_password(pwd, hashed_pwd)


def test_verify_password_with_wrong_password():
    pwd = 'test'
    hashed_pwd = Hasher.get_password_hash(pwd)

    assert not Hasher.verify_password('wrong', hashed_pwd)
