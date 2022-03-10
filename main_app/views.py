from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RestaurantForm
from .models import Restaurant
from .restaurants import Cart

def main_page(request):
    return render(request,'main.html',{})

@login_required
def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form=RestaurantForm()
    return render(request,'add_restaurant.html',{'form':form})

@login_required
def pick_restaurant(request):
    restaurants = Cart(request)
    cookies = restaurants.get_values().keys()
    restaurants_to_random = Restaurant.objects.all().exclude(id__in=cookies).order_by('?')
    if len(restaurants_to_random)==0:
        restaurants.clear()
        restaurants_to_random = Restaurant.objects.all().exclude(id__in=cookies).order_by('?')
    selected_item = restaurants_to_random[0]
    restaurants.add(selected_item.id)

    return render(request,'pick_restaurant.html',{'selected_item':selected_item})

@login_required
def all_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request,'all_restaurants.html',{'restaurants':restaurants})

@login_required
def picked_for_user(request):
    restaurants = Cart(request)
    cookies_keys = restaurants.get_values().keys()
    cookies = Restaurant.objects.filter(id__in=cookies_keys)
    return render(request,'picked_for_user.html',{'cookies':cookies})
