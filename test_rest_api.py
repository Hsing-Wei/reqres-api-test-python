import pytest
import requests

def register_unsuccessful_data():
    return [
        {
            "email": "eve.holt@reqres.in",
            "password": "",
        },
        {
            "email": "",
            "password": "cityslicka",
        },
        {
            "email": "",
            "password": "",
        },
        {
            "email": "email",
            "password": "password",
        },
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslickacityslickacityslicka",
        },
    ]

@pytest.mark.parametrize('email, passwd',
                         [('eve.holt@reqres.in', 'cityslicka'),])
def test_api_register_successful(email, passwd):
    data = {'email': email,
            'password': passwd}
    resp = requests.post(url="https://reqres.in/api/register", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : "\
        + str(resp.status_code)
    assert data['token'] is not None, "token is None."

@pytest.mark.parametrize("email, passwd",register_unsuccessful_data())
def test_api_register_unsuccessful(email, passwd):
    data = {'email': email,
            'password': passwd}
    resp = requests.post(url="https://reqres.in/api/register", data=data)
    data = resp.json()
    assert (resp.status_code == 400), "Status code is not 400. Rather found : "\
        + str(resp.status_code)
