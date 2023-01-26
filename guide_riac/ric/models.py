from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Radar(models.Model):
    '''Модель РЛС'''
    title = models.CharField('Название РЛС', max_length=250) # Название РЛС
    slug = models.SlugField('URL', null=False, unique=True) #Слаг
    body = models.TextField('Описание РЛС', null=True) # Описание РЛС
    data = models.DateTimeField('Дата', auto_now=True) # Дата создание записи
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''Функция перевода названия РЛС (русских букв) в слаг (на английском)'''
        if not self.slug:
            self.slug = slugify(self.title)
        super(Radar, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''Функция получения URL к РЛС'''
        return reverse('ric:radar_detail', args={self.slug})

    class Meta:
        verbose_name = 'РЛС' # Название РЛС ед. число
        verbose_name_plural = 'РЛС' # Название РЛС мн. число