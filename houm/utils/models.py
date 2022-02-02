# django
from django.contrib.gis.db import models


class BModel(models.Model):
    """
    Proxy Utilities model.
    This models is abstract model to provide timestamp info.
    All models inherit from this.
    """

    created = models.DateTimeField(
        "created_at", auto_now_add=True, help_text="Fecha de creacion"
    )
    modified = models.DateTimeField(
        "modified_at", auto_now=True, help_text="Fecha de ultima modificacion"
    )

    class Meta:
        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-modified"]