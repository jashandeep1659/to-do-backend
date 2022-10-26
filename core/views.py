from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import mixins
from .serializers import ToDO_serializers
from .models import ToDo
from user.models import User


class Todo_ViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ToDo.objects.all()
    serializer_class = ToDO_serializers

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["user"] = user.id
        print(data)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Created")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
