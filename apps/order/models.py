from django.db import models
import uuid
from user.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(unique=True, default=1)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    products = models.JSONField()
    systemRecomends = models.JSONField(default={})
    MLRecomends = models.JSONField(default={})
    statisticRecomends = models.JSONField(default={})

    class Meta:
        verbose_name = ('Заказ')
        verbose_name_plural = ('Заказы')
