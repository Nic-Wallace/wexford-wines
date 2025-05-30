from django.db import models


class Newsletter(models.Model):
    """
    newsletter model
    """
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.email
