from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'treasurehunt/home.html')

def leaderboard(request):
    return render(request, 'treasurehunt/leaderboard.html', {'title': 'leaderbaord'})

def task_one(request):
    return render(request, 'treasurehunt/task_one.html', {'title': 'One'})

def task_two(request):
    return render(request, 'treasurehunt/task_two.html', {'title': 'Two'})

def end(request):
    return render(request, 'treasurehunt/end.html', {'title': 'end'})