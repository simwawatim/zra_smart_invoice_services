from django.urls import include, path
from .views import auth_view

urlpatterns = [
    path('auth/', auth_view, name='auth_view'),
]
