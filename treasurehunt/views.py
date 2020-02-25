from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic

from .forms import teamForm
from .models import Team


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


class leaderboard(generic.ListView):
    model = Team
    template_name = 'treasurehunt/leaderboard.html'

def howtoplay(request):
    return render(request, 'treasurehunt/howtoplay.html', {'title': 'How to Play'})


def clue(request):
    return render(request, 'treasurehunt/clue.html')


def task(request):
    return render(request, 'treasurehunt/task.html', {'title': 'Task'})

def qr(request):
    return render(request, 'treasurehunt/qr.html', {'title': 'QR'})

def info(request):
    return render(request, 'treasurehunt/info.html', {'title': 'Info'})


def end(request):
    return render(request, 'treasurehunt/end.html', {'title': 'End'})