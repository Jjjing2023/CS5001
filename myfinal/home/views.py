from django.shortcuts import render, redirect
from .utils import get_astro_type
from django.urls import reverse
from .models import Sign


def home(request):
    astro_type = None
    if request.method == 'POST':
        name = request.POST.get('name')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')

        # Calculate astro type based on birthdate
        birthdate_parts = birthdate.split('-')
        astro_type = get_astro_type(
            int(birthdate_parts[1]), int(birthdate_parts[2]))

        # pass birthdate to the result view
        return redirect('result', astro_type=astro_type)

    return render(request, 'home/home.html', {'astro_type': astro_type})


def result(request):
    astro_type = request.GET.get('astro_type')
    sign_objects = Sign.objects.all()
    context = {
        'astro_type': astro_type,
        'sign_objects': sign_objects
    }

    # retrieve all sign objects from the database

    # search code
    return render(request, 'home/result.html', context)
