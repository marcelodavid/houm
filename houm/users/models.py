# django
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.validators import RegexValidator

# utils
from houm.utils.models import BModel


class User(BModel, AbstractUser):
    """
    Default custom user model for houm.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={"unique": "Ya existe un usuario con este email."},
    )
    phone_regex = RegexValidator(
        regex=r"\+?5?\d{9,15}$",
        message="El formato deber ser: +5959******. Con un maximo de 15 digitos",
    )
    phone = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "uid"]
    uid = models.CharField(
        "user id",
        help_text="User identification number",
        max_length=50,
        unique=True,
        db_index=True,
        error_messages={"unique": "Ya existe un usuario con esta credencial"},
    )
    direction = models.CharField(max_length=150, blank=True, null=True)
    is_houmer = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
