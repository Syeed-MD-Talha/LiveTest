from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/<int:id>', views.detail_page, name='detail'),
    path('create', views.create_contact, name='create'),
    path('edit_delete', views.edit_delete, name='edit_delete'),
    path('edit/<int:id>', views.edit_contact, name='edit'),
    path('delete/<int:id>', views.delete_contact, name='delete'),
    path('search/', views.search_contact, name='search'),
]
