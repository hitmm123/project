from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name="homepage"),
    path('add/', views.add, name="addur"),
    path('delete/<int:pos>', views.delete, name="delete"),


]
