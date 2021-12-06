from django.shortcuts import render

from api.models import Arduino


def landing(request):

    return render(
        request,
        'single_pages/landing.html'
    )
