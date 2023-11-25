"""
URL configuration for tts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name= "home"),
    path("auth/", include('users.urls')),
    path("board/", include('board.urls')),
    path("yes/", views.yes, name='yes'),
    path("choice/", views.choice, name='choice'),
    path("koreaQ/", views.koreaQ, name='koreaQ'),
    path("engQ/", views.engQ, name='engQ'),
    path("right_kor/", views.right_kor, name='right_kor'),
    path("right_eng/", views.right_eng, name='right_eng'),
    path("wrong_kor/", views.wrong_kor, name='wrong_kor'),
    path("wrong_eng/", views.wrong_eng, name='wrong_eng'),
    path("loading_ccd/", views.loading_ccd, name='loading_ccd'),
    path("loading_jjd/", views.loading_jjd, name='loading_jjd'),
    path("loading_jld/", views.loading_jld, name='loading_jld'),
    path("loading_ksd/", views.loading_ksd, name='loading_ksd'),
    path("loading_kwd/", views.loading_kwd, name='loading_kwd'),
    path("data_dashboard/", views.data_dashboard, name='data_dashboard')
]
