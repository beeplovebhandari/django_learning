from django.urls import path
from .views import home, python, test, name, temp1, portfolio, login

urlpatterns = [
    path("world/", test),
    path("python/", python),
    path("test/", name),
    path("temp/", temp1),
    path("portfolio/", portfolio),
    path("login/", login),
    path("", home)
]