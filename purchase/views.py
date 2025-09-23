from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from services.zra_client import SmartInvoiceClient


class GetPurchases(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        client = SmartInvoiceClient()
        purchase_data = request.data
        result = client.get_purchases(purchase_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_200_OK)

class SavePurchase(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        client = SmartInvoiceClient()
        purchase_data = request.data
        result = client.save_purchase(purchase_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_200_OK)
