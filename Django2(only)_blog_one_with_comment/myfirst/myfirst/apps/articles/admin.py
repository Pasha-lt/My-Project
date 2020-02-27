from django.contrib import admin

from .models import Article, Comment

admin.site.register(Article) # добавляем в админку возможность управлять статьями.
admin.site.register(Comment) # добавляем в админку возможность управлять комментариями.