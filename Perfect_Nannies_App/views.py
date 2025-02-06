from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Perfect_Nannies_App.models import User
from Perfect_Nannies_App.serializers import NannyRegistrationSerializer, GuardianRegistrationSerializer, \
    NannyLoginSerializer, GuardianLoginSerializer


class NannyRegistrationViewSet(APIView):
    def post(self, request):
        serializer = NannyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message: Registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuardianRegistrationViewSet(APIView):
    def post(self, request):
        serializer = GuardianRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message: Registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NannyLoginViewSet(APIView):
    def post(self, request):
        serializer = NannyLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    login(request, user)
                    return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

             # user = authenticate(username=username, password=password)
            # print(f"User found: {user}")
            # user = User.objects.filter(username="nan1").first()
            # #
            # print(user)  # Should not be None
            # print(user.is_active)
            # print(check_password("actual_password", user.password))
            # user.set_password("faithful")
            # user.save()

        #     if user:
        #         login(request, user)
        #         return Response({"message": "Login successful"}, status=status.HTTP_201_CREATED)
        #     return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        #
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuardianLoginViewSet(APIView):
    def post(self, request):
        serializer = GuardianLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    login(request, user)
                    return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # user = authenticate(username=username, password=password)
        #     if user:
        #         login(request, user)
        #         return Response({"message": "Login Successful"}, status=status.HTTP_201_CREATED)
        #     # return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

