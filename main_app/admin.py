from django.contrib import admin
from .models import Restaurant, StoreCookies

@admin.register(Restaurant)
class RestaurantRegister(admin.ModelAdmin):
    list_display = ['name','phone_number']

admin.site.register(StoreCookies)
