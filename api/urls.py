from django.urls import path

from api import views

urlpatterns = [
    path('arduino/', views.ArduinoView.as_view()),
    # path('ph/now', views.nowPHView.as_view()),
]