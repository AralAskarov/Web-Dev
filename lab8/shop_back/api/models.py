from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products', default=None )
    name = models.CharField('Название', max_length=50)
    price = models.FloatField('Цена')
    description  = models.TextField('Описание')
    count  = models.IntegerField('Количество')
    is_active = models.BooleanField('Можно ли купить')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


