import random
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


class HealthCheckView(APIView):
    """
    Эндпоинт проверки работоспособности сервиса.
    GET /api/health/
    """
    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "koticback",
                "cats_count": Cat.objects.count(),
            },
            status=status.HTTP_200_OK,
        )


class CatViewSet(viewsets.ModelViewSet):
    """
    API для управления котиками.
    - GET /api/cats/ — список котиков (с пагинацией)
    - POST /api/cats/ — добавить котика
    - GET /api/cats/<id>/ — получить информацию о котике
    - PUT/PATCH /api/cats/<id>/ — обновить информацию
    - DELETE /api/cats/<id>/ — удалить котика
    - GET /api/cats/random/ — получить случайного котика
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        """Возвращает случайного котика."""
        ids = list(Cat.objects.values_list('id', flat=True))
        if not ids:
            return Response(
                {"detail": "Котиков пока нет в базе данных."},
                status=status.HTTP_404_NOT_FOUND,
            )
        random_id = random.choice(ids)
        cat = Cat.objects.get(id=random_id)
        serializer = self.get_serializer(cat)
        return Response(serializer.data)
