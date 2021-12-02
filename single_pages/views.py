from django.shortcuts import render

from blog.models import Post


def landing(request):
    return render(
        request,
        'single_pages/landing.html',

    )
