from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='listView'),
    path('<slug:id>/', views.detail, name='detail')

]
