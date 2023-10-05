from django.shortcuts import render,redirect
from .models import User,Event,Submission
from .forms import SubmissionForm
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

def account(request):
    user = request.user
    context = {'user':user}
    return render(request, 'account.html', context)

def event(request,pk):
    event = Event.objects.get(id=pk)
    submitted = Submission.objects.filter(participant = request.user,event=event).exists()
    registered = request.user.events.filter(id=event.id).exists()
    

    context = {'event':event, 'registered':registered, 'submitted':submitted}
    return render(request,'event.html',context)

def registration_confirmation(request,pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk = event.id)

    context = {'event':event}
    return render(request, 'event_confirmation.html',context )

def project_submission_form(request,pk):
    event = Event.objects.get(id=pk)

    form = SubmissionForm()

    if request.method=='POST':
        form = SubmissionForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant = request.user
            submission.event = event
            submission.save()
            return redirect('account')

    context = {'event':event,'form': form}
    return render(request,'submit.html',context)

#Add Owner Authentications
def update_project_form(request,pk):
    submission = Submission.objects.get(id=pk)
    event = submission.event
    form = SubmissionForm(instance=submission)

    if request.method=='POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form,'event':event}
    return render(request,'submit.html',context)

