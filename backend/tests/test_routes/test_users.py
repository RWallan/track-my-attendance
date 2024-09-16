from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'Test User',
            'course': 'Test',
            'period': '1 period',
            'email': 'test@test.com',
            'password': 'testtest',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['id'] == 1
    assert 'password' not in response.json()


def test_create_user_with_created_email(client, user):
    response = client.post(
        '/users/',
        json={
            'name': 'Test User',
            'course': 'Test',
            'period': '1 period',
            'email': user.email,
            'password': 'testtest',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists.'}


def test_create_user_with_small_pwd(client):
    response = client.post(
        '/users/',
        json={
            'name': 'Test User',
            'course': 'Test',
            'period': '1 period',
            'email': 'test@test.com',
            'password': 'tt',
        },
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_create_user_with_large_pwd(client):
    response = client.post(
        '/users/',
        json={
            'name': 'Test User',
            'course': 'Test',
            'period': '1 period',
            'email': 'test@test.com',
            'password': 't' * 50,
        },
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_update_user(client, token):
    response = client.put(
        '/users/me',
        json={'name': 'Updated User', 'password': 'newpassword'},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'Updated User'
