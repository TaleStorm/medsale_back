from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=16)

    class Meta:
        verbose_name = ('Пользователь')
        verbose_name_plural = ('Пользователи')
