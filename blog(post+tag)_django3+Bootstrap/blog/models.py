from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    # db_index индексация ускорит поиск.
    title = models.CharField(max_length=150, db_index=True)
    # unique=True требования уникальности.
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    # blank=True Обозначает что поле может быть пустым.
    body = models.TextField(blank=True, db_index=True)
    # auto_now_add=True будет сохранять когда в бд будет добавлятся.
    date_pub = models.DateTimeField(auto_now_add=True)
    # Связываем Tag и Post. Передаем ему с чем связываем и ставим blank=True если не будет параметров.
    # Третим аргументом пишем обозначает то свойство которое появится у екземпляра Tag
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id: # Если у конкретного экземпляра модели нет нет свойства id(Если статья не было создано еще)
            self.slug = gen_slug(self.title)# Тогда вызываем функцию
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title  # return self.title

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']