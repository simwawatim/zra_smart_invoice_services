from django.urls import path
from . import views

app_name = "codes"

urlpatterns = [
    path(
        'api/get-unit-of-measure-code/<str:code_name>/',
        views.UnitOfMeasureDetailByCodeName.as_view(),
        name='unitofmeasure-detail-by-codename'
    ),
    path(
        'api/packaging-unit-code/<str:code_name>/',
        views.PackagingUnitCodeDetail.as_view(),
        name='packaging-unit-code-detail'
    ),
    path(
        'api/country-code/<str:name>/',
        views.GetCountryCodeByName.as_view(),
        name='country-detail-by-name'
    ),
]
