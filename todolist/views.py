from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from todolist.models import ToDo
from todolist.serializers import ToDo_Serializer, Test_Serializer
from rest_framework import status

# Create your views here.


class login_View(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })


class Todo_View(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = ToDo.objects.filter(author=request.user)
        serializer = ToDo_Serializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Test_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        todo = ToDo.objects.filter(id=request.data['id'])
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        todo = ToDo.objects.filter(id=request.data['id']).first()
        serializer = Test_Serializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
