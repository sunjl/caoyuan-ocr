import sys

import os

sys.path.append(os.path.realpath('..'))


class User:
    def __init__(self, id, display_name, username, password, roles, active, create_date, update_date):
        self.id = id
        self.display_name = display_name
        self.username = username
        self.password = password
        self.roles = roles
        self.active = active
        self.create_date = create_date
        self.update_date = update_date

    def add_role(self, role):
        self.roles.append(role)


class Role:
    def __init__(self, id, name, introduction):
        self.id = id
        self.name = name
        self.introduction = introduction
