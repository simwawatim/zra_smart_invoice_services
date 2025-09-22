from django.urls import path
from .views import SaveItemView

app_name = "items"
urlpatterns = [
    path('api/saveItem/', SaveItemView.as_view(), name='save_item'),
]
