from django.contrib import admin
from .models import Clue, Task, Answer, Location, Team, Route,RouteLocationMapping

admin.site.register(Clue)
admin.site.register(Task)
admin.site.register(Answer)
admin.site.register(Location)
admin.site.register(Team)
admin.site.register(Route)
admin.site.register(RouteLocationMapping)