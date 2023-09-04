from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UserSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'User Created Successfully. Now perform Login to get your token',
        })


class HomeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        try:
            # Your view logic here
            return render(request, 'index.html')
        except AuthenticationFailed:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)