from django.urls import path
from .views import index, InfoView

urlpatterns = [
    path('', index),
    path('data', InfoView.as_view())
]
