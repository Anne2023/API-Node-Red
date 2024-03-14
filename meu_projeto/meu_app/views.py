# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dados
from .serializers import DadosSerializer

class DadosAPIView(APIView):
    def get(self, request):
        dados = Dados.objects.first()  # Supondo que há apenas um conjunto de dados
        serializer = DadosSerializer(dados)
        return Response(serializer.data)
