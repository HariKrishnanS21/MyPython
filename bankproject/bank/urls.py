from django.urls import path
from . import views
app_name='bank'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('form/',views.forms,name='forms'),
    path('logout/',views.logout,name='logout')

]