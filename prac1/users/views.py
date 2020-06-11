from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import ugettext_lazy

from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(detail=True)
    # def logout(self, request):
    #     try:
    #         request.user.auth_token.delete()
    #     except (AttributeError, ObjectDoesNotExist):
    #         pass
    #
    #     logout(request)
    #
    #     return Response({"success": "Successfully logged out."},
    #                     status=status.HTTP_204_NO_CONTENT)

    @action(detail=False)
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response({"detail": ugettext_lazy("Successfully logged out.")},
                            status=status.HTTP_200_OK)

        return response

    def get_permissions(self):

        if self.action == 'create':
            return [AllowAny()]
        elif self.action in ['update', 'destroy']:
            return [AllowAny()]

        return super().get_permissions()
