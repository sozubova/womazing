from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    # path('', include('django.contrib.auth.urls'))
]
