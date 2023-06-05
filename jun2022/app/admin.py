from django.contrib import admin
from . import models


class FoodInline(admin.StackedInline):
    model = models.Food
    extra = 1


class FoodAdmin(admin.ModelAdmin):
    exclude = ["author"]

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.author = request.user

        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj is not None and obj.author == request.user


class CategoryAdmin(admin.ModelAdmin):
    inlines = [FoodInline]
    list_display = ["name"]

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]


admin.site.register(models.Food, FoodAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Sale)
admin.site.register(models.ProductSale)
