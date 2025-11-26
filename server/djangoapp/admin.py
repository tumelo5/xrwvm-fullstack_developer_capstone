from django.contrib import admin
from .models import CarMake, CarModel


# Inline CarModel inside CarMake admin page
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# CarMake admin customization
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description', 'country')
    search_fields = ('name', 'country')


# CarModel admin customization
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)


# Register the models so they show in admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
