from django.urls import path
from . import views

urlpatterns = [
    path('', views.system_root_page, name='system.urls'),
]