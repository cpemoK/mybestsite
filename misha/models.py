from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ServiceType(models.Model):
    type = models.CharField(max_length=80)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'

    def __str__(self):
        return f'{self.type}'


class Services(models.Model):
    title = models.CharField(max_length=150)
    descript = models.DecimalField(max_digits=19, decimal_places=2)
    img = models.URLField()
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.title} {self.created_at}'
