from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Card(models.Model):
    status = models.BooleanField(default=False)
    score = models.IntegerField()
    limit = models.FloatField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)