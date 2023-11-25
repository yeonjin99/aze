from django.urls import path
from . import views


urlpatterns= [
    path("index/", views.index, name= "index"),
    path("insert/", views.insert, name="insert"),
    path("detail/<int:id>", views.detail, name='detail'),
    path("update/<int:id>", views.update, name='update'),
    path("delete/<int:id>", views.delete, name='delete'),
]