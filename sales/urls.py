from django.urls import path
from .views import SaveNormalSale

app_name = "sale"
urlpatterns = [
    path('api/normal-sale/', SaveNormalSale.as_view())
]
