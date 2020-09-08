from django.urls import path
from .views import *

urlpatterns = [
    path('',todolist,name='todolist'),
    path('<int:activity_id>/', mark , name='completed'),
    path('<int:activity_id>/edit/', edit , name='edit'),
    path('<int:activity_id>/delete/', delete , name='delete'),
]