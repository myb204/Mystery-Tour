from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'treasurehunt/home.html')

def start(request):
    return render(request, 'treasurehunt/start.html')

def leaderboard(request):
    return render(request, 'treasurehunt/leaderboard.html', {'title': 'Leaderboard'})

def clue(request):
    return render(request, 'treasurehunt/clue.html')

def task_one(request):
    return render(request, 'treasurehunt/task_one.html', {'title': 'Task'})

def info(request):
    return render(request, 'treasurehunt/info.html', {'title': 'Info'})

def end(request):
    return render(request, 'treasurehunt/end.html', {'title': 'End'})

