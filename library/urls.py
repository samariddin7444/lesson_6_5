from django.urls import path, include
from .views import library_view

urlpatterns = [
    path('library/', library_view,)
]