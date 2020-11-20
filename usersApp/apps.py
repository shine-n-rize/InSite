from django.apps import AppConfig


class UsersappConfig(AppConfig):
    name = 'usersApp'

    def ready(self):
        from usersApp import signals
