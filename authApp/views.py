import requests
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.views import ScopedProtectedResourceView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_provider.decorators import protected_resource
from django.contrib.auth.models import User as BaseUser
from authApp.serializers import TokenSerializer
from authApp.models import User


class MyView(ScopedProtectedResourceView, APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    # Write scope is required in token for calling the below created method.
    required_scopes = ['write']

    @staticmethod
    def get(_):
        breakpoint()
        return Response({"msg": "My get method"})

    @staticmethod
    def post(_):
        return Response({"msg": "My post method"})

    @staticmethod
    def put(_):
        return Response({"msg": "My put method"})

    @staticmethod
    def delete(_):
        return Response({"msg": "My delete method"})


@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
@protected_resource(scopes=['read'])
def fetch_record(request):
    # Read scope is required in token for this view.
    return Response({"msg": "fetch record view"})


@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@protected_resource(scopes=['create'])
def create_record(request):
    # create scope is required in token for this view.
    return Response({"msg": "create record view"})


@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
@protected_resource(scopes=['reset'])
def reset_record(request):
    # reset scope is required in token for this view.
    return Response({"msg": "reset record view"})


@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
@protected_resource(scopes=['edit'])
def edit_record(request):
    # edit scope is required in token for this view.
    return Response({"msg": "edit record view"})


@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
@protected_resource(scopes=['delete'])
def delete_record(request):
    # delete scope is required in token for this view.
    return Response({"msg": "delete record view"})


@api_view(["POST"])
def generate_token(request):
    """
    Method for generate auth2 token.
    """
    try:
        serial_data = TokenSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            data = serial_data.data
            # Fetching django auth user.
            base_user = BaseUser.objects.get(username=data["username"])
            # Fetching custom user for user scopes.
            user = User.objects.get(base_user=base_user)
            scopes = user.user_type
            data.update({"scope": scopes})
            url = request.build_absolute_uri("/auth/token/")
            response = requests.post(url, data)
            return Response(response.json(), response.status_code)
    except BaseUser.DoesNotExist:
        return Response({"Error": "Base user not available"}, status=400)

    except User.DoesNotExist:
        return Response({"Error": "User not available"}, status=400)