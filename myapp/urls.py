from django.urls import path
from .views import home, python, test, name, temp1, portfolio

urlpatterns = [
    path("world/", test),
    path("python/", python),
    path("test/", name),
    path("temp/", temp1),
    path("portfolio/", portfolio),
    path("", home)
]