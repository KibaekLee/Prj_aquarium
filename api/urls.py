from django.urls import path

from api import views

urlpatterns = [
    path('ph/', views.PHView.as_view()),
]