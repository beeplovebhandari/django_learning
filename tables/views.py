from django.shortcuts import render
from django.http import HttpResponse

from.models import Students

def student(request):
    students = Students.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})
