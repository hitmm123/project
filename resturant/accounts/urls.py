from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.AccountLogin.as_view(), name="login"),
    #path('add/', views.add, name="addur"),
    #path('delete/<int:pos>', views.delete, name="delete"),
]
