from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.getUser, name='getUser'),
    path('list', views.listUser, name="listUser"),
]