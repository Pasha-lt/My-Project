from django.urls import path

from  . import views  # ' .' - Обозначает что импортируем с корневой папки.

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), # переходим в views и ищем там index
    path('<int:article_id>/', views.detail, name='detail'), # Цифра запомнится и уже
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),

]