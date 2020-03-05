from django.contrib import admin
from .models import Clue, Task, Location, Team, Route

admin.site.register(Clue)
admin.site.register(Task)
admin.site.register(Location)
admin.site.register(Team)
admin.site.register(Route)
