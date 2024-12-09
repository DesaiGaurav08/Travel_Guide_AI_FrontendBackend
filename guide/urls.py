from django.urls import path
from travelling.urls import views as travel_views
from . import views

urlpatterns = [

    path("", travel_views.home),

    path('registration/', views.guide_registration, name='guide_registration'),
    path('login/', views.guide_login, name='guide_login'),
    path('dashboard/', views.guide_dashboard, name='guide_dashboard'),
    path('edit-profile/', views.guide_edit_profile, name='guide_edit_profile'),
    path('logout/', views.guide_logout, name='guide_logout'),

    path('get-doctor/', views.get_doctors , name='get_doctors'),
    path('edit-doctor/<int:doctor_id>', views.update_doctor_details, name='guide_edit_doctor'),
    path('delete-doctor/<int:doctor_id>', views.delete_doctor, name='delete_doctor'),

    path('get-place-info/', views.get_place_info, name='get_place_info'),
    path('update-place-info/<int:place_id>', views.update_place_info, name='update_place_info'),
    path('get-image/', views.get_images, name='get_images'),
    path('add-image/', views.add_place_image, name='add_place_image'),
    path('delete-image', views.delete_place_image, name='delete_place_image'),

    path("contact_support/", views.contact_support, name='contact_support'),

]
