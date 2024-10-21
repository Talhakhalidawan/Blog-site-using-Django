from django.urls import path
from application import views

urlpatterns = [
    path("" , views.home , name = "home"),
    path("create-post/" , views.createPost , name = "create-post"),
    path("about/" , views.about , name = "about"),
    path("logout/" , views.logout , name = "logout"),
    path("admin/" , views.admin , name = "admin"),
    path("update/<int:uid>" , views.update , name = "update"),
    path("delete/<int:uid>" , views.delete , name = "delete"),
]
