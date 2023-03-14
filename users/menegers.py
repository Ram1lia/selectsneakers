from django.contrib.auth.models import (
    BaseUserManager,
)


class MyUserManager(BaseUserManager):
    def _create_user(self, username, nickname, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели ваше имя Пользователя!")
        if not nickname:
            raise ValueError("Вы не ввели Никнейм!")
        if not password:
            raise ValueError("Вы не придумали Пароль!")
        user = self.model(
            username=username,
            nickname=nickname,
            password=password,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self,
            username,
            nickname,
            password=None,
            **extra_fields
    ):

        return self._create_user(username, nickname, password, is_staff=False, is_superuser=False, **extra_fields)


class polo():
    pass
