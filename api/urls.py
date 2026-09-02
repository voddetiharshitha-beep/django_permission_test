from django.urls import path
from .views import AdminOnlyView

urlpatterns = [
    path('admin-only/', AdminOnlyView.as_view()),
]