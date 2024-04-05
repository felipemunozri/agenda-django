from django.urls import path
from . import views

# app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='tasks'),
    path('<int:num>', views.index, name='tasks'),
    path('detail/<int:id>', views.detail, name='tasks_detail'),
    path('create/', views.create, name='tasks_create'),
    path('edit/<int:id>', views.edit, name='tasks_edit'),
    path('delete/<int:id>', views.delete, name='tasks_delete'),
]