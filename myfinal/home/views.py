"""
This module contains views for the astrology app.
"""
from django.shortcuts import render, redirect, HttpResponse
from .utils import get_astro_type, astro_dict_desc, astro_dict_url
from django.urls import reverse
from .models import Sign


def home(request):
    """
    Renders the home page of the astrology app.
    Parameters:
    - request: HTTP request object
    Returns:
    - Rendered template for the home page
    """
    return render(request, 'home/home.html')


def result(request):
    """
    Processes the user input and returns the corresponding astrology type, description and url.
    If the request method is POST, the function extracts user input and calculates the astrology type
    using the `get_astro_type()` function from the `utils.py` module.
    It then returns the `result.html` template with the extracted user input, astrology type, description, and url in
    the `context` dictionary.
    Parameters:
    - request: HTTP request object
    Returns:
    - Rendered template for the result page
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')

        # Calculate astro type based on birthdate
        birthdate_parts = birthdate.split('-')
        astro_type = get_astro_type(
            int(birthdate_parts[1]), int(birthdate_parts[2]))

        description = astro_dict_desc[astro_type]
        my_url = astro_dict_url[astro_type]

        context = {
            'name': name,
            'astro_type': astro_type,
            'description': description,
            'my_url': my_url
        }

        # pass birthdate to the result view
        return render(request, 'home/result.html', context)


def detail(request, sign_id):
    """
    Retrieves a `Sign` object from the database using the provided `sign_id` parameter.
    Returns the `detail.html` template with the `Sign` object in the `context` dictionary.
    Parameters:
    - request: HTTP request object
    - sign_id: ID of the `Sign` object to retrieve from the database
    Returns:
    - Rendered template for the detail page
    """
    sign = Sign.objects.get(pk=sign_id)
    context = {
        'sign': sign
    }
    return render(request, 'home/detail.html', context)
