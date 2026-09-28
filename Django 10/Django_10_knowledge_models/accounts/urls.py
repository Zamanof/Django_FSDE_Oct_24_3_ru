from django.urls import path

from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='register'),
    path('register/success/',register_success_view,name='register_success'),
    path('dashboard/',dashboard_view,name='dashboard'),
]