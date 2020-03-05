from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic import FormView

from .forms import teamForm, taskForm, routeForm
from .models import Team, Task, Location, Clue


def home(request):
    return render(request, 'treasurehunt/home.html')


def help(request):
    return render(request, 'treasurehunt/help.html')


def about(request):
    return render(request, 'treasurehunt/about.html')


def faqs(request):
    return render(request, 'treasurehunt/faqs.html')


def assistance(request):
    return render(request, 'treasurehunt/assistance.html')


class leaderboard(generic.ListView):
    model = Team
    template_name = 'treasurehunt/leaderboard.html'


def howtoplay(request):
    return render(request, 'treasurehunt/howtoplay.html', {'title': 'How to Play'})


def start(request):
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            form.save()
            teamName = form.cleaned_data.get('teamName')
            messages.success(request, f'Team created: {teamName}')
            return redirect('treasurehunt-howtoplay')
    else:
        form = teamForm()

    return render(request, 'treasurehunt/start.html', {'form': form})


def qr(request):
    return render(request, 'treasurehunt/qr.html', {'title': 'QR'})


def clue(request):
    return render(request, 'treasurehunt/clue.html')


def newroute(request):
    if request.method == 'POST':
        form = routeForm(request.POST)
        if form.is_valid():
            form.save()
            routeName = form.cleaned_data.get('routeName')
            messages.success(request, f'Route Created: {routeName}')
            return redirect('treasurehunt-home')

    else:
        form = routeForm()

    return render(request, 'treasurehunt/newroute.html', {'form': form})


class ClueDetailView(generic.DetailView):
    model = Clue
    template_name = 'treasurehunt/clue.html'


def task(request):
    #if request.method == 'POST':
    #form =
    return render(request, 'treasurehunt/task.html', {'title': 'Task'})


class TaskDetailView(FormView):
    form = taskForm
    #model = Task
    template_name = 'treasurehunt/task.html'


def info(request):
    return render(request, 'treasurehunt/info.html', {'title': 'Info'})


class InfoDetailView(generic.DetailView):
    model = Location
    template_name = 'treasurehunt/info.html'


def end(request):
    return render(request, 'treasurehunt/end.html', {'title': 'End'})


def admin(request):
    return render(request, 'treasurehunt/admin')


def blog(request):
    return render(request, 'treasurehunt/bloghome.html', {'title': 'Blog: Home'})