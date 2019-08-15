from django.contrib import admin
from .models import Task, Label, Event


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'due_at', 'get_labels')

    def get_labels(self, obj):
        return '[{}]'.format(",".join([l.name for l in obj.labels.all()]))
    get_labels.short_description = 'labels'


class LabelAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Event, EventAdmin)
