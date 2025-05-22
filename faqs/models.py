from django.db import models


class FAQ(models.Model):
    """
    FAQ model
    """
    question = models.CharField(max_length=200, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question
