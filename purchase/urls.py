from django.urls import path
from purchase import views

app_name = "purchase"
urlpatterns = [
    path('api/purchases/get/', views.GetPurchases.as_view(), name='get-purchases'),
    path('api/purchases/save/', views.SavePurchase.as_view(), name='save-purchase'),
]
