from django.apps import AppConfig


class AuthuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authuser'
    verbose_name = "Users"


    def ready(self) -> None:
        import authuser.signals
