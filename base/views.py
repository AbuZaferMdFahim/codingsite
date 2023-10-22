from django.shortcuts import render,redirect,HttpResponse
from .models import User,Event,Submission
from .forms import SubmissionForm,CustomerUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signin(request):
    page = 'signin'
    if request.method =="POST":
        user = authenticate(email=request.POST['email'],password = request.POST['password'])

        if user is not None:
            login(request,user)
            return redirect('home')

    context = {'page':page}
    return render(request, 'login_register.html', context)

def signup(request):
    form = CustomerUserCreationForm()
    if request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')

    page = 'signup'

    context = {'page':page, 'form':form} 
    return render(request, 'login_register.html', context)

def signout(request):
    logout(request)
    return redirect('signin')

def home(request):
    users = User.objects.filter(hackathon_participant=True)
    events = Event.objects.all()
    context = {'users': users , 'events':events}  
    return render(request,'home.html',context)

def profile(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def account(request):
    user = request.user
    context = {'user':user}
    return render(request, 'account.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)  # You can replace 'id' with the appropriate field or attribute in Event
    submitted = Submission.objects.filter(participant=request.user, event=event).exists()
    registered = request.user.events.filter(id=event.id).exists()

    context = {'event': event, 'registered': registered, 'submitted': submitted}
    return render(request, 'event.html', context)


@login_required()
def registration_confirmation(request,pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk = event.id)

    context = {'event':event}
    return render(request, 'event_confirmation.html',context )

@login_required()
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
@login_required()
def update_project_form(request,pk):
    submission = Submission.objects.get(id=pk)
    if request.user != submission.participant:
        return HttpResponse("You Can't be Here")

    event = submission.event
    form = SubmissionForm(instance=submission)

    if request.method=='POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form,'event':event}
    return render(request,'submit.html',context)

