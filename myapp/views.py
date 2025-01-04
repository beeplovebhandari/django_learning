from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, template_name="mytemp/home.html")

def test(request):
    return HttpResponse("Hello World")

def python(request):
    name = request.GET.get("name")
    print(name)
    return HttpResponse("<h1>I'am Learning Python</h1>")

# def home(request):
#     content = """
#     <h1>Hello World</h1>
#     <h2>This my home page</h2>
#     <p>Python and django are awesome</p>
#     """
#     return HttpResponse(content)

def name(request):
    # We can send query strings / query parameters in the urls
    # Everything sent after "?" in the url is querrystring
    # Query strings can be multiple and are seperated by ampersand (&)
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"<h1>Hello my name is {name} and age is {age} </h1>")



def temp1(request):
    return render (request, template_name="mytemp/temp1.html")