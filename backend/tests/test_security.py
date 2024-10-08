from http import HTTPStatus

import jwt
from freezegun import freeze_time

from backend.helpers.settings import settings
from backend.security import JWT, Hasher


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


def test_update_user_with_invalid_token(client):
    response = client.put(
        '/users/me',
        json={'name': 'Updated User', 'password': 'newpassword'},
        headers={'Authorization': 'Bearer 123'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_update_user_with_invalid_user(client, token, session, user):
    session.delete(user)
    session.commit()

    response = client.put(
        '/users/me',
        json={'name': 'Updated User', 'password': 'newpassword'},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_update_user_with_wrong_token(client):
    wrong_token = JWT.encode({'sub': ''})

    response = client.put(
        '/users/me',
        json={'name': 'Updated User'},
        headers={'Authorization': f'Bearer {wrong_token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_expired_token(client, user):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            '/auth/token',
            data={'username': user.email, 'password': user.plain_pwd},
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']

    with freeze_time('2023-07-14 12:31:00'):
        response = client.put(
            '/users/me',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'email': 'wrong@wrong.com',
                'password': 'wrongwrong',
            },
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}
