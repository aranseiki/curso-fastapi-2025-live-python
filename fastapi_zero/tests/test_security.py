from http import HTTPStatus

from jwt import decode

from fastapi_zero.security import (
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
    get_current_user,
)


def test_jwt():
    data = {'test': 'test'}

    token = create_access_token(data)
    decoded = decode(token, SECRET_KEY, algorithms=ALGORITHM)

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1',
        headers={'Authorization': 'Bearer token-invalido'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_invalid_token_without_subject():
    data = {'test': 'test'}

    token = create_access_token(data)
    decoded = decode(token, SECRET_KEY, algorithms=ALGORITHM)

    result_current_user = ''
    try:
        result_current_user = get_current_user(token=token)
    except Exception as erro:
        result_current_user = erro

    assert result_current_user.status_code == HTTPStatus.UNAUTHORIZED
    assert result_current_user.detail == 'Could not validate credentials'
    assert 'sub' not in decoded
