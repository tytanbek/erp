from django.contrib import admin
from .models import Direction, TimeSlot, Application


admin.site.register(Direction)
admin.site.register(TimeSlot)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'direction', 'time_slot', 'status', 'created_at')
    list_filter = ('direction', 'time_slot', 'status')
