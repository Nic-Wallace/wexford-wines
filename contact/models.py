from django.db import models


class Contact(models.Model):
    """
    contact model
    """
    email = models.EmailField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=75, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
