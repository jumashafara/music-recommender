from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "premus"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('/prediction', views.prediction, name="prediction")
]
