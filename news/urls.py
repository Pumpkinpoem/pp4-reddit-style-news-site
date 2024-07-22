from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create_post'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_username/', views.change_username, name='change_username'),
    path('change_email/', views.change_email, name='change_email'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('settings/', views.account_settings, name='account_settings'),
    path('profile/', views.account_profile, name='account_profile'),
]
