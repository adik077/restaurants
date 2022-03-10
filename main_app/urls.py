from django.urls import path
from .views import main_page, add_restaurant, pick_restaurant, all_restaurants,picked_for_user

urlpatterns = [
    path('',main_page, name='main'),
    path('add_restaurant/',add_restaurant, name='add_restaurant'),
    path('pick_restaurant/',pick_restaurant, name='pick_restaurant'),
    path('all_restaurants/',all_restaurants, name='all_restaurants'),
    path('picked_for_user/',picked_for_user, name='picked_for_user'),
]