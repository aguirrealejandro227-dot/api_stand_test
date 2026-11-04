import requests
import configuration
import data


def post_user_body(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


def get_users_table():
    return requests.get(
        configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    )

