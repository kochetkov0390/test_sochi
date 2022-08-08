from rest_framework.decorators import action
from rest_framework.response import Response

from . import service
from .serializers import FanSerializer


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Поставить лайк."""
        obj = self.get_object()
        service.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Удалить лайк."""
        obj = self.get_object()
        service.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """Лайкнувшие пользователи."""
        obj = self.get_object()
        fans = service.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)
