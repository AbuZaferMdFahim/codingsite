from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('event/<str:pk>/',views.event,name="event"),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('registration_confirmation/<str:pk>/',views.registration_confirmation,name="registration_confirmation"),
]
