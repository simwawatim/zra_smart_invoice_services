from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from services.zra_client import SmartInvoiceClient 

class SaveNormalSale(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        sales_data = request.data
        ZRA_CLIENT_INSTANCE = SmartInvoiceClient()
        result = ZRA_CLIENT_INSTANCE.save_sale(sales_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    

class SaveCreditNote(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        sales_data = request.data
        ZRA_CLIENT_INSTANCE = SmartInvoiceClient()
        result = ZRA_CLIENT_INSTANCE.save_sale(sales_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    
class SaveDebitNote(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        sales_data = request.data
        ZRA_CLIENT_INSTANCE = SmartInvoiceClient()
        result = ZRA_CLIENT_INSTANCE.save_sale(sales_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
    

