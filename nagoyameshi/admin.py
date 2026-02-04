from django.contrib import admin
from .models import Category, Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)