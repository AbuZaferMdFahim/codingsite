from django.shortcuts import render,redirect
from .models import User,Event,Submission
# Create your views here.

def home(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()
    context = {'users': users , 'events':events}  
    return render(request,'home.html',context)

def profile(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'profile.html',context)

def event(request,pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request,'event.html',context)

def registration_confirmation(request,pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk = event.id)

    context = {'event':event}
    return render(request, 'event_confirmation.html',context )
