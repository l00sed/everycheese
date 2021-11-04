from django.urls import path
from . import views


app_name = "cheeses"
urlpatterns = [
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    # URL Patter for the CheeseCreateView
    path(
        route='add/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),
    # URL Pattern for the CheeseDetailView
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for updating view
    path(
        route='<slug:slug>/update/',
        view=views.CheeseUpdateView.as_view(),
        name='update'
    ),
]
