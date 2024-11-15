from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.exceptions import handle_exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

# Model
from django.contrib.auth import get_user_model, hashers
User = get_user_model()

# Create your views here.
class SignUpView(APIView):

    @handle_exceptions
    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        return Response({
            'message': 'Signup successful',
            'user': new_user.data
        })
  
class SignInView(APIView):

    @handle_exceptions
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Find the user matching email
        user = User.objects.get(username=username)

        # Check the plain text password from the request body against the stored hash
        # Takes plain text as first argument, hash as second
        if hashers.check_password(password, user.password):
            # Generate token using simpleJWT
            token_pair = RefreshToken.for_user(user)

            serialized_user = UserSerializer(user)

            return Response({ 
                'user': serialized_user.data,
                'token': str(token_pair.access_token)
            })
        
        # Send 401 if passwords don't match
        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)