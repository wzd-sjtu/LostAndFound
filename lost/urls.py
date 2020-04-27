from django.urls import path
from . import views
import total_page.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('kind/<kind_name_slug>/', views.kind, name='kind'),
    path('add_kind/', views.add_kind, name='add_category'),
    path('add_page/<kind_name_slug>/', views.add_page, name='add_page'),
    path('logout/',views.user_logout, name='logout'),
    #  可以通过name参数，来进行url映射，提高便捷性
    path('data_fresh/',views.data_fresh,name = 'data_fresh'),
    path('make/',views.make,name="make")
]