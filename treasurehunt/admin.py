from django.contrib import admin
from .models import Clue, Task, Location, Route, RouteLocationMapping, Team, Game

admin.site.register(Clue)
admin.site.register(Task)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(RouteLocationMapping)
admin.site.register(Team)
admin.site.register(Game)
