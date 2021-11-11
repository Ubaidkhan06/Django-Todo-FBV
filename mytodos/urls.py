from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView , name='home'),
    path('update/<int:id>/', views.UpdateView , name='update'),
    path('delete/<int:id>/', views.DeleteView , name='delete'),
]