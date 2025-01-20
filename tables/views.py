from django.shortcuts import render
from django.http import HttpResponse
from.models import Student, Item

def student(request):
    students = Student.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})


def classroom(request):
    return HttpResponse("<h1> Hello World </h1>")



def item(request):
    a = Item.objects.all()
    return render (request, template_name="tables/items.html", context={"items":a})


