from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # username = request.POST['username']
            # password = request.POST['password']
            user = auth.authenticate(username=username,  # обязательно писать через равно, иначе ошибка!!
                                     password=password)  # аутентификация, есть ли с атким именем и паролем пользвоатель
            if user:
                auth.login(request, user)  # если польхователь есть, то он авторизуется
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             auth.login(request, user)
#             context = {'user': user}
#             return HttpResponseRedirect(reverse('homepage'))
#         else:
#             context = {'user': None}
#             return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))  # когда зарегался, отправляем на страницу входа
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    # form = UserLoginForm()
    # context = {'form': form}
    return render(request, 'users/profile.html')
