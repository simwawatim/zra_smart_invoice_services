from django.urls import path
from .views import SaveStockView

app_name = "stock"
urlpatterns = [
    path('api/save-stock/', SaveStockView.as_view())
]
