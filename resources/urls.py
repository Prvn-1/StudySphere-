from django.urls import path
from . import views

urlpatterns = []
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resource, name='upload_resource'),
    path('list/', views.resource_list, name='resource_list'),
    path('manage/', views.manage_resources, name='manage_resources'),
    path('approve/<int:resource_id>/', views.approve_resource, name='approve_resource'),
    path('reject/<int:resource_id>/', views.reject_resource, name='reject_resource'),
    path('<int:pk>/', views.resource_detail, name='resource_detail'),
    path('<int:pk>/download/', views.download_resource, name='download_resource'),
    path('<int:pk>/rate/', views.rate_resource, name='rate_resource'),
    path('edit/<int:pk>/', views.resource_edit, name='resource_edit'),
    path('delete/<int:pk>/', views.resource_delete, name='resource_delete'),
]
