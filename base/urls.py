from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),

    # Authentication start
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    # Authentication End

    path('account/',views.account,name="account"),
    path('event/<str:pk>/',views.event,name="event"),
    path('profile/<str:pk>/',views.profile,name="profile"),

    # About Registration 
    path('registration_confirmation/<str:pk>/',views.registration_confirmation,name="registration_confirmation"),
    path('project_submission_form/<str:pk>/',views.project_submission_form,name="project_submission_form"),
    path('update_project_form/<str:pk>/',views.update_project_form,name="update_project_form"),

]
