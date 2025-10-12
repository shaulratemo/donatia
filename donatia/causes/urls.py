from django.urls import path
from . import views

urlpatterns = [
    path('', views.CauseListCreateView.as_view(), name='cause-list-create'),
    path('<int:pk>/', views.CauseDetailView.as_view(), name='cause-detail'),
]
