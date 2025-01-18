from django.urls import path 
from.views import student, classroom, item

urlpatterns = [
    path ("student/", student, name="student"),
    path ("classroom/", classroom, name="classroom"),
    path("item/", item, name="item")
]