from django.db import models
import uuid


def photo_upload_path(instance, filename: str) -> str:
    """
    Общий путь для фото.
    """
    return (f'{instance.title}/photos/{filename}')


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to=photo_upload_path,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=0)
    preparation = models.TextField()
    recomends = models.JSONField(default={}, blank=True, null=True)

    class Meta:
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукты')
