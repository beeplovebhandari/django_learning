from django.shortcuts import render




def main(request):
    people=[
        {"name": "Ram", "age": 30, "address": "KTM"},
        {"name": "Hari", "age": 24, "address": "BKT"},
        {"name": "Sita", "age": 45, "address": "PKR"}
    ]
    return render (request, template_name= 'temp_inheritance/home.html',     context= {"people": people})



def features(request):
    items= [
        {"name": "Laptop", "feature": "A portable computer that can be used anywhere"},
        {"name": "Mouse", "feature": "A clicking input deviceof computer"},
        {"name": "Keyboard", "feature": "An Input device with keys "}
    ]
    return render (request, template_name='temp_inheritance/features.html', context={"items": items})

