from django.urls import path
from . import views

# app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='contacts'),
    path('<str:letter>', views.index, name='contacts'),
    path('detail/<int:id>', views.detail, name='contacts_detail'),
    path('create/', views.create, name='contacts_create'),
    path('edit/<int:id>', views.edit, name='contacts_edit'),
    path('delete/<int:id>', views.delete, name='contacts_delete'),
]