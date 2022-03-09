from django.urls import path
from .views import FelixListView, FelixDetailView, FelixCreateView, FelixUpdateView, FelixDeleteView

urlpatterns = [
    path('', FelixListView.as_view(), name='felix_list'),
    path('<int:pk>/', FelixDetailView.as_view(), name='felix_detail'),
    path('create/', FelixCreateView.as_view(), name='felix_create'),
    path('<int:pk>/update/', FelixUpdateView.as_view(), name='felix_update'),
    path('<int:pk>/delete/', FelixDeleteView.as_view(), name='felix_delete'),
]