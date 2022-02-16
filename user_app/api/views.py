from os import stat
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializers
from rest_framework.response import Response
from rest_framework import status
from user_app import models

@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':

        serializers = RegistrationSerializers(data=request.data)
        data = {}

        if serializers.is_valid():
            account = serializers.save()

            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        
        else:
            data = serializers.errors

        return Response(data)