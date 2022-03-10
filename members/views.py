from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import views as auth_views, login, authenticate, logout
from main_app.restaurants import Cart
from main_app.models import StoreCookies

def login_user(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                ############
                try:
                    cookies = StoreCookies.objects.get(user=request.user)
                    cookies_dict={}
                    new_string=cookies.cookies.split(',')

                    print(new_string)
                    for item in new_string:
                        cookies_dict[item]=item
                    request.session[settings.CART_SESSION_ID] = cookies_dict
                except Exception:
                    pass
                ############
                return HttpResponseRedirect(reverse('main'))
        return render(request, 'registration/login.html', {})

def logout_user(request):
    cookies = Cart(request)
    c=cookies.get_values()
    to_database = []
    for item in c:
        to_database.append(item)
    joined=','.join(to_database)
    saved = joined
    try:
        storing_object = StoreCookies.objects.get(user=request.user)
        storing_object.cookies = saved
        storing_object.save()
    except Exception:
        StoreCookies.objects.create(user=request.user,cookies=saved)
    print(saved)
    logout(request)
    return HttpResponseRedirect(reverse('main'))


class Register(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('login')

class UpdateUserInfo(UpdateView):
    template_name = 'registration/update_profile.html'
    form_class = UpdateUserForm
    def get_success_url(self):
        return reverse_lazy('main')

    def get_object(self):
        return self.request.user


class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('change_password_done')


def change_password_done(request):
    return render(request,'registration/change_password_done.html',{})