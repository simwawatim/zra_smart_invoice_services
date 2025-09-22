from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import format_item_data  
from rest_framework.permissions import AllowAny
from services.zra_client import send_item_to_smart_invoice  

class SaveItemView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        item_data = format_item_data(request.data)
        result = send_item_to_smart_invoice(item_data)
        if 'error' in result:
            return Response({"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_201_CREATED)
