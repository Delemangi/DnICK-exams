from django.contrib import admin
from . import models


class CollaborationInline(admin.StackedInline):
    model = models.Collaboration
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    inlines = [CollaborationInline]
    exclude = ["user"]
    list_display = ["name"]

    def has_change_permission(self, request, obj=None):
        return obj is not None and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.user = request.user

        super().save_model(request, obj, form, change)


class PilotAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]


admin.site.register(models.Airline, AirlineAdmin)
admin.site.register(models.Pilot, PilotAdmin)
admin.site.register(models.Balloon)
admin.site.register(models.Flight)
