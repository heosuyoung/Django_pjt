from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True,
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'  # 충돌 방지용
