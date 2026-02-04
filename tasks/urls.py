from django.urls import path,include
from . import views
app_name='tasks'
urlpatterns = [
    path('', views.project_list, name='project_list'),
]