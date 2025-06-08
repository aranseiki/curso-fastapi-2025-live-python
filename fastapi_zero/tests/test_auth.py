from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        'auth/token/',
        data={'username': user.email, 'password': user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_login_for_access_token_unauthorized_by_email(client, user, token):
    response = client.post(
        'auth/token/',
        data={'username': 'bob@example.com', 'password': user.clean_password},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_login_for_access_token_unauthorized_by_password(client, user, token):
    response = client.post(
        'auth/token/',
        data={'username': user.email, 'password': 'secret'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}
