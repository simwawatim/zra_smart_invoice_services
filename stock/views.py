from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from services.zra_client import SmartInvoiceClient



class SaveStockView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        stock_data = request.data
        client = SmartInvoiceClient()
        result = client.save_stock(stock_data)

        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    



class SaveStockMaster(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        stock_master_data = request.data
        client = SmartInvoiceClient()
        result = client.save_stock_master(stock_master_data)

        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_201_CREATED)