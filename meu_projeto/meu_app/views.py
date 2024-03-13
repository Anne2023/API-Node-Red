from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
