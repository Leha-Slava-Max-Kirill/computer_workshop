from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('computers/', views.ComputerListView.as_view(), name='computers'),
    path('computer/<int:pk>', views.ComputerDetailView.as_view(), name='computer-detail'),
    path('cpus/', views.CpuListView.as_view(), name='cpus'),

    path('filtered/', views.GetCoresListView.as_view(), name='filtered'),
    path('computers_filter/', views.ComputersFilteredListView.as_view(), name='computers_filter'),

    path('cpu/<int:pk>', views.CpuDetailView.as_view(), name='cpu-detail'),
    path('gpus/', views.GpuListView.as_view(), name='gpus'),
    path('gpu/<int:pk>', views.GpuDetailView.as_view(), name='gpu-detail'),
    path('rams/', views.RamListView.as_view(), name='rams'),
    path('ram/<int:pk>', views.RamDetailView.as_view(), name='ram-detail'),
]