from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, username, email=None, password=None):
        """
        Creates and saves a User with the given phone_number, username,
        email and password.
        """
        if not phone_number:
            raise ValueError("Users must have a phone number")

        if not username:
            raise ValueError("Users must have an username")
        
        user = self.model(
            phone_number=phone_number,
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, email=None, password=None):
        """
        Creates and saves a superuser with the given phone_number, username,
        email and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user