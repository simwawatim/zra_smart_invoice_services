from django.urls import path
from customer import views

app_name = "customer"
urlpatterns = [
    path('api/customers/get/', views.GetCustomer.as_view()),
    path('api/customers/save/', views.SaveBranchCustomer.as_view()),
]
