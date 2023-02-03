from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index),
    path('register/', views.register),
    path('<int:pk>', login_required(views.chatview), name='contact_chat'),
    path('left', views.leftuser, name='leftuser'),
    path('profile', views.profile, name='profile')
]
