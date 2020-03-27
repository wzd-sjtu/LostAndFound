from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('kind/<kind_name_slug>/', views.kind, name='kind'),
    path('add_kind/', views.add_kind, name='add_category'),
    path('add_page/<kind_name_slug>/', views.add_page, name='add_page'),
    path('logout/',views.user_logout, name='logout'),
]