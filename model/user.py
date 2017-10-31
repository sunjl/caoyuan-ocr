import sys

import os

sys.path.append(os.path.realpath('..'))


class User:
    def __init__(self, id, display_name, email, username, password,
                 auth_token, auth_roles, active, create_date, update_date):
        self.id = id
        self.display_name = display_name
        self.email = email
        self.username = username
        self.password = password
        self.auth_token = auth_token
        self.auth_roles = auth_roles
        self.active = active
        self.create_date = create_date
        self.update_date = update_date

    def add_auth_role(self, auth_role):
        self.auth_roles.append(auth_role)


class Role:
    def __init__(self, id, name, introduction):
        self.id = id
        self.name = name
        self.introduction = introduction
