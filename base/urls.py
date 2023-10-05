from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('account/',views.account,name="account"),
    path('event/<str:pk>/',views.event,name="event"),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('registration_confirmation/<str:pk>/',views.registration_confirmation,name="registration_confirmation"),
    path('project_submission_form/<str:pk>/',views.project_submission_form,name="project_submission_form"),
    path('update_project_form/<str:pk>/',views.update_project_form,name="update_project_form"),

]
