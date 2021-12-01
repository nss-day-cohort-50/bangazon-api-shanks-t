from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    like = models.BooleanField(default=False)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, )
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='liked')
