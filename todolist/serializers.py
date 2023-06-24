from rest_framework import serializers
from todolist.models import ToDo


class ToDo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class Test_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ['author',]

    def create(self, validated_data):

        return super().create(validated_data)
