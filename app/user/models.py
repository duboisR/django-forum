from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import gettext_lazy as _


# Custom Auth
# https://docs.djangoproject.com/fr/3.0/topics/auth/customizing/
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_("Adresse Email"),
        max_length=255,
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to='avatar',
        blank=True, null=True,
    )
    first_name = models.CharField(
        verbose_name=_("Prénom"),
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name=_("Nom"),
        max_length=255,
    )

    username = None
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    class Meta:
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")

    def __str__(self):
        return self.email

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_avatar_url(self):
        if self.avatar and self.avatar.file:
            return self.avatar.url
        return staticfiles_storage.url('img/avatar.png')
