from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.new),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.one_show),
    path('shows/<int:id>/edit', views.edit_show_page),
    path('shows/<int:id>/process_edit', views.process_edit),
    path('shows/<int:id>/delete', views.delete_show)
]
