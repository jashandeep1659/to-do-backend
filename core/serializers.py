from rest_framework import serializers
from user.models import User
from .models import ToDo


class ToDO_serializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
