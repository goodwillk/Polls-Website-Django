from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.form_register, name='form_register'),
    path('login/', views.form_login, name='form_login'),
    path('logout/', views.log_out, name='log_out'),
]