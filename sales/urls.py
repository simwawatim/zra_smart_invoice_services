from django.urls import path
from .views import SaveCreditNote, SaveDebitNote, SaveNormalSale

app_name = "sale"
urlpatterns = [
    path('api/normal-sale/', SaveNormalSale.as_view()),
    path('api/create-note/', SaveCreditNote.as_view()),
    path('api/debit-note/', SaveDebitNote.as_view()),
]
