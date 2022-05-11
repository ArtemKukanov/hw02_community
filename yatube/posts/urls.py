from django.urls import path
from . import views

app_name = 'ways_posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='way_group'),
    path('', views.index, name='way_index')
]
