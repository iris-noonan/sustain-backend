from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from django.contrib.auth import get_user_model
User = get_user_model()

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionDenied as e:
            return Response({ 'detail': str(e) }, status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist as e:
            print(e)
            return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)
        except ValidationError as e:
            print(e)
            return Response(e.detail, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print('Error name:', e.__class__.__name__)
            return Response({ 'detail': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper