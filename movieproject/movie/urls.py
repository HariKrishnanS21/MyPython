from django.urls import path
from . import views
app_name='movie'

urlpatterns = [

    path('',views.home,name='home'),
    path('movie/<int:mov_id>',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('del/<int:id>',views.delete,name='delete')
]