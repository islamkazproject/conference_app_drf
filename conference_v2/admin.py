from django.contrib import admin
from .models import Presentation, Room, Schedule, UserScheduleRelation

admin.site.register(Presentation)
admin.site.register(Room)
admin.site.register(Schedule)
admin.site.register(UserScheduleRelation)