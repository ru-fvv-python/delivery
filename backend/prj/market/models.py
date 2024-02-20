from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Provider(User):
    """ Поставщик """

    name = models.CharField(max_length=250, default='', db_index=True,
                            unique=True,
                            verbose_name='Наименование', )
    phone = models.CharField(max_length=250, default='', db_index=True,
                             unique=True,
                             verbose_name='Телефон')
    rating = models.IntegerField(default=0, db_index=True,
                                 verbose_name='Рейтинг')

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class Consumer(User):
    """ Потребитель """

    name = models.CharField(max_length=250, default='', db_index=True,
                            unique=True,
                            verbose_name='Наименование', )
    phone = models.CharField(max_length=250, default='', db_index=True,
                             unique=True,
                             verbose_name='Телефон')
    address = models.TextField(default='', verbose_name='Адрес')
    geo_location = models.CharField(max_length=250, default='', db_index=True,
                                    verbose_name='Геолокация')

    class Meta:
        ordering = ['name']
        verbose_name = 'Потребитель'
        verbose_name_plural = 'Потребители'

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Категория """

    name = models.CharField(max_length=250, default='', db_index=True,
                            unique=True,
                            verbose_name='Наименование', )

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Продукция """

    name = models.CharField(max_length=250, default='', db_index=True,
                            unique=True,
                            verbose_name='Наименование', )
    image = models.ImageField(upload_to='product', blank=True,
                              verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Категория')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)


class Store(models.Model):
    """ Склад """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Продукция')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,
                                 verbose_name='Поставщик')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')

    class Meta:
        ordering = ['product__name', ]
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return '%s (%s)' % (self.product, self.provider)


class Order(models.Model):
    """ Заказ """
    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE,
                                 verbose_name='Потребитель')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата обновления')
    status = models.CharField(max_length=10, default='new', db_index=True,
                              choices=STATUS,
                              verbose_name='Статус')

    class Meta:
        ordering = ('-created_at', 'consumer__name')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    """ Состав заказа """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Продукция')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Заказ')
    amount = models.IntegerField(default=0,
                                 verbose_name='Количество')

    class Meta:
        ordering = ['product__name', ]
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Составы заказов'
