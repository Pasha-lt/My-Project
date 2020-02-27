"""myfirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('articles.urls')), # articles/ - что пишем на сайте, второй аргумент пишем  что открывать,
#articles это папка в которой находится urls.py. Если мы просто укажем первым аргументом пустые скобки то тогда
# эта информация будет на главной.
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

]
