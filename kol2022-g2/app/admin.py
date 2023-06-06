from django.contrib import admin
from . import models


class SpecializationInline(admin.StackedInline):
    model = models.Specialization
    extra = 1


class WorkshopAdmin(admin.ModelAdmin):
    inlines = [SpecializationInline]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RepairAdmin(admin.ModelAdmin):
    readonly_fields = ["user"]

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.user = request.user

        super().save_model(request, obj, form, change)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name"]

    def has_add_permission(self, request):
        return request.user.is_superuser


class CarAdmin(admin.ModelAdmin):
    list_display = ["type", "speed"]


admin.site.register(models.Workshop, WorkshopAdmin)
admin.site.register(models.Repair, RepairAdmin)
admin.site.register(models.Manufacturer, ManufacturerAdmin)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Specialization)
