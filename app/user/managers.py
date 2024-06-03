from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self, password, username, **extra_fields):
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, username, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(password, username, **extra_fields)

    def create_superuser(self, password, username, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(password, username, **extra_fields)
