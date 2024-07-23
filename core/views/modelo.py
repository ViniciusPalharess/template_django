from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import ModeloSerializer, ModeloWriteSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloWriteSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ModeloSerializer
        return ModeloWriteSerializer