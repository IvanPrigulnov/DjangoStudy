from django.db import models
from django.urls import reverse


# Create your models here.
class Animals(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='animal_image/%Y/%m/%d/', verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Экзотические животные'
        verbose_name_plural = 'Экзотические животные'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Класс')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Классы животных'
        verbose_name_plural = 'Классы животных'
        ordering = ['id']
