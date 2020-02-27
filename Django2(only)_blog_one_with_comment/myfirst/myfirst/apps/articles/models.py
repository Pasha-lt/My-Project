import datetime
from django.db import models

from django.utils import timezone
# Обьясняем джанге из чего состоит наше приложение и что джанге нужно хранить в базе данных.

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')


    def __str__(self):
        return self.article_title


    def was_published_recently(self):
        """Метод который выводит статьи за  последних фю7 дней"""
        return self.pub_date >= (timezone.now() - datetime.timedelta(days= 7))


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE) # так как комментарии должны к чему то крепится, крепим его к Article
    author_name = models.CharField('имя автора', max_length= 50)
    comment_text = models.CharField('текст комментария', max_length= 200)

    def __str__(self):
        return self.author_name


    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


