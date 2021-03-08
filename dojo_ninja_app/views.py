from django.shortcuts import render, HttpResponse, redirect
from dojo_ninja_app.models import Dojos, Ninjas

def home(request):
    context = {
        'dojos': Dojos.objects.all()
    }
    return render(request, "home.html", context)

def dojo_submit(request):
    Dojos.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
    )
    print(request.POST)
    return redirect('/')

def ninja_submit(request):
    Ninjas.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = Dojos.objects.get(id=request.POST['dojo']),
    )
    print(request.POST)
    return redirect('/')
