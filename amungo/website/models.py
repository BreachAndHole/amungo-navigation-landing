from django.db import models
from django.urls import reverse


class BaseProduct(models.Model):
    name = models.CharField('product name', max_length=100)
    slug = models.SlugField('URL')
    price_usd = models.PositiveIntegerField('price in USD')
    is_in_stock = models.BooleanField('is in stock')
    description = models.TextField('description', blank=True, null=True)


class BaseProductPhoto(models.Model):
    photo = models.ImageField('product photo', upload_to='photos/%Y/%m')
    is_title = models.BooleanField('is title photo')


class Board(BaseProduct):
    datasheet = models.FileField(
        'board\'s documentation',
        upload_to='datasheets',
        blank=True,
        null=True,
    )
    lead_time_weeks = models.PositiveSmallIntegerField(
        'standard lead time in weeks'
    )

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_slug': self.slug})


class BoardPhoto(BaseProductPhoto):
    board = models.ForeignKey(Board, verbose_name='board', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'board\'s photo'
        verbose_name_plural = 'board\'s photos'

    def __str__(self):
        return f'Photo {self.board}'

    @property
    def photo_url(self):
        return self.photo.url or ''


class VisitorMessage(models.Model):
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email')
    message = models.TextField('message')
    date = models.DateField('date message sent', auto_now_add=True)

    class Meta:
        verbose_name = 'visitor\'s message'
        verbose_name_plural = 'visitor\'s messages'

    def __str__(self):
        return f'{self.email}, {self.date}'
