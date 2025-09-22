from django.urls import path
from .views import SaveStockMaster, SaveStockView

app_name = "stock"
urlpatterns = [
    path('api/save-stock/', SaveStockView.as_view()),
    path('api/save-stock-master/', SaveStockMaster.as_view())
]
