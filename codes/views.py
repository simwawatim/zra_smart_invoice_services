from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from services.zra_client import SmartInvoiceClient


class GetCountryCodeByName(APIView):
    permission_classes = [AllowAny]

    def get(self, request, name):
        client = SmartInvoiceClient()
        result = client.get_country_code(name)

        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class UnitOfMeasureDetailByCodeName(APIView):
    permission_classes = [AllowAny]

    def get(self, request, code_name):
        client = SmartInvoiceClient()
        result = client.get_unit_of_measure(code_name)

        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
    

class PackagingUnitCodeDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, code_name):
        client = SmartInvoiceClient()
        result = client.get_packaging_unit_code(code_name)

        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
