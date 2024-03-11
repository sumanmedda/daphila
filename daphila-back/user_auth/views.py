from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, VerifyOTPSerializer
from .models import User
import random
from .utils import send_email_to_client


class UserRegistrationView(APIView):
    # Register User
    def post(self,request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                otp = random.randint(100000, 999999)
                send_email_to_client(otp,request.data['email'])
                return Response({"status":201,"message": "User registered successfully.Please Verify Your email using otp sent to your mail"}, status=status.HTTP_201_CREATED)
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message": serializer.error_messages},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
    
    # Update User
    def put(self, request, pk):
        try:
            userdata = User.objects.get(id=pk)
            serializer = UserSerializer(instance=userdata,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User updated successfully."}, status=status.HTTP_200_OK)
            return Response({"message": "Some Errors"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)

    # Delete User
    def delete(self, request, pk):
        userdata = User.objects.get(id=pk)
        userdata.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_200_OK)
        
    # Get All Users
    def get(self,request):
        userdata = User.objects.all()
        serializer = UserSerializer(userdata, many=True)
        return Response(serializer.data)


# Verify User
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyOTPSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
                if user[0].otp != otp:
                    return Response({"message": "Not a valid OTP"}, status=status.HTTP_400_BAD_REQUEST)
                user = user.first()
                user.verified = True
                user.save()
                return Response({"message": "User verified successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Some Error Occured"}, status=status.HTTP_400_BAD_REQUEST)
    
    

    
