from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.forms import inlineformset_factory

from .forms import teamForm, routeForm, routeMappingForm
from .models import Team, Task, Location, Clue, Route, RouteLocationMapping
from .filters import TeamFilter


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
            teamMembers = form.getTeamMembers()
            routeID = form.getSelectedRoute()
            request.session['teamName'] = teamName
            request.session['teamMembers'] = teamMembers
            request.session['routeID'] = routeID
            request.session['progress'] = 0

            messages.success(request, f'Team created: {teamName}')
            return redirect('treasurehunt-howtoplay')
    else:
        form = teamForm()

    return render(request, 'treasurehunt/start.html', {'form': form})


def leaderboard_search(request):
    team_list = Team.objects.all()
    team_filter = TeamFilter(request.GET, queryset=team_list)
    return render(request, 'treasurehunt/leaderboard.html', {'filter': team_filter})


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

    return render(request, 'treasurehunt/howtoplay.html', context)


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
            mapping = RouteLocationMapping.objects.filter(routeID=chosenRoute, orderInRoute=progress + 1)[0]

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


class ClueDetailView(generic.DetailView):
    model = Clue
    template_name = 'treasurehunt/clue.html'


def task(request):
    return render(request, 'treasurehunt/task.html', {'title': 'Task'})


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'treasurehunt/task.html'


def end(request):
    return render(request, 'treasurehunt/end.html', {'title': 'End'})


def admin(request):
    return render(request, 'treasurehunt/admin')


def qr(request):
    return render(request, 'treasurehunt/qr.html', {'title': 'QR'})


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


def blog(request):
    return render(request, 'treasurehunt/bloghome.html', {'title': 'Blog: Home'})
