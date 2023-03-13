from rest_framework import status
from rest_framework.response import Response
from .serializers import AccountSerializer, AccountValidateSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Account
from rest_framework import permissions


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        personal_area = Account.objects.create(**serializer.validated_data)
        personal_area.save()
        return Response(data={'message': 'data received',
                              'personal_area': self.serializer_class(personal_area).data})
