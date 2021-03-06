from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin
from django.views import generic
from django.forms import inlineformset_factory

from .forms import teamForm, routeForm, taskForm, routeMappingForm
from .models import Team, Task, Location, Clue, Route, RouteLocationMapping
from .filters import TeamFilter

""""
These functions return calls to render the corresponding page based on the user's request
"""
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

"""
This method handles the form data when the user starts a new game.
The cleaned data is retrieved from the form and the sessions for that game are established.
If the form was given invalid data, the empty form is returned and the user is informed of what to change.
"""
def start(request):
    if request.method == 'POST':
        form = teamForm(request.POST)
        if form.is_valid():
            form.save()
            teamName = form.cleaned_data.get('teamName')
            teamMembers = form.getTeamMembers()
            routeID = form.getSelectedRoute()
            request.session['teamName'] = teamName
            request.session['teamMembers'] = teamMembers
            request.session['routeID'] = routeID
            request.session['progress'] = 0
            return redirect('treasurehunt-howtoplay')
    else:
        form = teamForm()

    return render(request, 'treasurehunt/start.html', {'form': form})

"""
This method allows the filtering of different routes on the leaderboard tables
"""
def leaderboard_search(request):
    team_list = Team.objects.all()
    team_filter = TeamFilter(request.GET, queryset=team_list)
    return render(request, 'treasurehunt/leaderboard.html', {'filter': team_filter})

"""
This method writes a team's score to the database after having finished the game
"""
def end(request):
    context = {
        'Score': request.session['score']
    }

    name = request.session['teamName']
    team = Team.objects.filter(teamName=name)[0]
    team.score = request.session['score']
    team.save()

    return render(request, 'treasurehunt/end.html', context)

"""
This method establishes the first clue to be given to the user after they successfully add their team
"""
def howtoplay(request):
    context = {
        'Clue': Clue.objects.all(),
    }

    route = request.session['routeID']
    chosenRoute = Route.objects.filter(routeName=route)[0]
    firstMapping = RouteLocationMapping.objects.filter(routeID=chosenRoute, orderInRoute=1)[0]
    firstClue = firstMapping.locationID.clueID.id
    context['firstClue'] = firstClue

    # Setting currentLocation session variable to be 1
    request.session['currentLocation'] = firstClue
    request.session['progress'] = 1
    request.session['score'] = 0

    return render(request, 'treasurehunt/howtoplay.html', context)

"""
This class-based view allows different information pages to be presented based on the current location
"""
class InfoDetailView(generic.DetailView):
    model = Location
    template_name = 'treasurehunt/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Location'] = Clue.objects.all()
        context['Clue'] = Clue.objects.all()

        route = self.request.session['routeID']
        progress = self.request.session['progress']
        chosenRoute = Route.objects.filter(routeName=route)[0]

        if progress < chosenRoute.numOfLocations:
            mapping = RouteLocationMapping.objects.filter(routeID=chosenRoute, orderInRoute=progress+1)[0]

        else:
            mapping = RouteLocationMapping.objects.filter(routeID=chosenRoute, orderInRoute=progress)[0]

        nextClue = mapping.locationID.clueID.id
        context['nextClue'] = nextClue

        context['routeLength'] = chosenRoute.numOfLocations
        context['progress'] = progress

        # Setting currentLocation session variable to be the next one
        self.request.session['currentLocation'] = nextClue

        # Setting progress to be the most recently visited location
        self.request.session['progress'] = mapping.orderInRoute

        return context

"""
This class-based view allows different clue pages to be presented based on the current location.
"""
class ClueDetailView(generic.DetailView):
    model = Clue
    template_name = 'treasurehunt/clue.html'

"""
This class-based view allows different task pages to be presented based on the current location.
It also handles the taskForm to present the user with multiple-choice answers for that task dynamically.
"""
class TaskDetailView(FormMixin, DetailView):
    model = Task
    template_name = 'treasurehunt/task.html'
    form_class = taskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Location'] = Location.objects.all()
        context['progress'] = self.request.session['progress']
        return context

    def get_form(self, *args, **kwargs):
        currentLocation = self.request.session['currentLocation']
        currentTask = Task.objects.filter(id=currentLocation)[0]
        self.task = currentTask
        form_class = self.form_class

        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super(TaskDetailView, self).get_form_kwargs()
        return dict(kwargs, task=self.task)

    def form_valid(self, form):
        guess = form.cleaned_data['answers']
        isCorrect = self.task.checkCorrect(guess)

        if isCorrect:
            self.request.session['score'] += 10
            nextInfo = self.get_success_url()
            return HttpResponseRedirect(nextInfo)
        else:
            self.request.session['score'] -= 5
        messages.error(self.request, "Incorrect, try again! 5 points deducted!")
        return super(TaskDetailView, self).get(self, self.request)

    def get_success_url(self):
        return reverse('treasurehunt-info-detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def admin(request):
    return render(request, 'treasurehunt/admin')


def qr(request):
    return render(request, 'treasurehunt/qr.html', {'title': 'QR'})


"""
This method handles the request from the user when they add a new custom route to the database
"""
def newroute(request):
    mappingFormSet = inlineformset_factory(Route, RouteLocationMapping,
                                           routeMappingForm,
                                           fields=('locationID',),
                                           can_delete=False,
                                           min_num=2,
                                           extra=10)
    if request.method == 'POST':
        form1 = routeForm(request.POST)
        form2set = mappingFormSet(request.POST, request.FILES)
        if form1.is_valid() and form2set.is_valid():
            route = form1.save(commit=False)  # Get route instance
            form2set = form2set.save(commit=False)  # Save form don't write to database
            route.numOfLocations = len(form2set)  # Set numLocations
            route.save()

            counter = 1
            for form in form2set:
                mapObject = form  # Create route mapping object
                mapObject.routeID = route  # Assign route to mapping object
                mapObject.orderInRoute = counter  # Assign a order
                form.save()  # Save the form to the database
                counter += 1

            routeName = form1.cleaned_data.get('routeName')
            messages.success(request, f'Route Created: {routeName}')
            return redirect('treasurehunt-home')

    else:
        form1 = routeForm()
        form2set = mappingFormSet()

    return render(request, 'treasurehunt/newroute.html', {'form1': form1,
                                                          'form2': form2set})

