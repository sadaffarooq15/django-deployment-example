"""firstt_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from first_app import views
urlpatterns = [
    path('',views.index, name='index'),
    path("first_app/", include('first_app.urls')),
    path("admin/", admin.site.urls),
]
#this urls uses path instead of url so donot right in regular expression and thats why i have left an empty '' in there and then it worked!!!
#to quit server just press cntl + c