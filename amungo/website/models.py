from django.db import models
from django.urls import reverse


class BaseProduct(models.Model):
    name = models.CharField('название', max_length=100)
    slug = models.SlugField('URL')
    price_usd = models.PositiveIntegerField('цена, USD')
    is_in_stock = models.BooleanField('есть в наличии')
    description = models.TextField('описание', blank=True, null=True)


class BaseProductPhoto(models.Model):
    photo = models.ImageField('фото', upload_to='photos/%Y/%m')
    is_title = models.BooleanField('является главной')


class Board(BaseProduct):
    datasheet = models.FileField(
        'документация',
        upload_to='datasheets',
        blank=True,
        null=True,
    )
    lead_time_weeks = models.PositiveSmallIntegerField(
        'стандартное время отгрузки, недель'
    )

    class Meta:
        verbose_name = 'плата'
        verbose_name_plural = 'платы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_slug': self.slug})


class BoardPhoto(BaseProductPhoto):
    board = models.ForeignKey(Board, verbose_name='плата', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'фото платы'
        verbose_name_plural = 'фото плат'

    def __str__(self):
        return f'Photo {self.board}'


class VisitorMessage(models.Model):
    name = models.CharField('имя', max_length=50)
    email = models.EmailField('email')
    message = models.TextField('сообщение')
    date = models.DateField('дата посещения', auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение посетителя'
        verbose_name_plural = 'сообщения посетителей'

    def __str__(self):
        return f'{self.email}, {self.date}'
