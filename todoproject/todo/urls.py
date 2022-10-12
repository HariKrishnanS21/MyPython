from . import views
from django.urls import path
app_name='todo'
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='del'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('cbvhome/',views.lw.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.dw.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.uw.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.dlw.as_view(),name='cbvdelete'),
    ]