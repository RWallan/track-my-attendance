from http import HTTPStatus


def test_get_access_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.plain_pwd},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['token_type'] == 'bearer'
    assert response.json()['access_token']


def test_wrong_email(client, user):
    response = client.post(
        '/auth/token',
        data={'username': 'test@test.com', 'password': user.plain_pwd},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email.'}


def test_wrong_password(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': 'wrong'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect password.'}
