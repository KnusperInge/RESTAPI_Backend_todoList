from rest_framework import serializers
from todolist.models import ToDo


class ToDo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
