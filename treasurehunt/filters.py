from .models import Team
import django_filters

class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = ['routeID']
