from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from services.zra_client import SmartInvoiceClient


class GetCustomer(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        client = SmartInvoiceClient()
        customer_data = request.data
        result = client.get_customer(customer_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_200_OK)

class SaveBranchCustomer(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        client = SmartInvoiceClient()
        customer_data = request.data
        result = client.save_branch_customer(customer_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_200_OK)
