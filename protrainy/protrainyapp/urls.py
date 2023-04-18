from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [


    path("create",views.create),
    path('test',views.test),
    path("create", views.create),
    path("read", views.read),
    path("edit", views.edit),
    path("login", views.login),
    path("delete", views.delete),


]