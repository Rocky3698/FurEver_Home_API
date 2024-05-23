from django.contrib.auth import login, logout,authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserLoginSerializer,UserSerializer
from rest_framework import status,viewsets,generics
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from .models import UserAccount

#user/register
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(request.data)
            if user:
                token = Token.objects.create(user=user)
                return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print(request.data,serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user/login
class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username= username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id,'role':user.role})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user/
class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#user/logoout
class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'success' : "logout successful"},status=status.HTTP_200_OK)


#shelters/toprated
class TopRatedUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return UserAccount.objects.order_by('-rating')[:10]