from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    path('display_laptop/',views.display_Laptop,name='display_laptop'),
    path('display_Desktop/',views.display_Desktop,name='display_Desktop'),
    path('display_Mobile/',views.display_Mobile,name='display_Mobile'),

    path('add_laptop/',views.add_laptop,name='add_laptop'),
    path('add_desktop/',views.add_desktop,name='add_desktop'),
    path('add_mobile/',views.add_mobile,name='add_mobile'),

    path('edit_laptop/<str:pk>/',views.edit_laptop,name='edit_laptop'),
    path('edit_desktop/<str:pk>/',views.edit_desktop,name='edit_desktop'),
    path('edit_mobile/<str:pk>/',views.edit_mobile,name='edit_mobile'),

    path('delete_laptop/<str:pk>/',views.delete_laptop,name='delete_laptop'),
    path('delete_desktop/<str:pk>/',views.delete_desktop,name='delete_desktop'),
    path('delete_mobile/<str:pk>/',views.delete_mobile,name='delete_mobile'),

]
