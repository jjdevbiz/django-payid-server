from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import LocalPayIdEntity
from .serializers import LocalPayIdEntitySerializer

class LocalPayIdViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LocalPayIdEntity.objects
    serializer_class = None
    lookup_field = 'name'
    lookup_value_regex = '[\w\-\_]+' # # FIXME -- Incomplete. Other chars plus some unicode are OK.

    def list(self, request, *args, **kwargs):
        # This endpoint is not a part of the PayID Protocol.
        #
        # This code returns a list of all of the payIdURIs managed by the server.
        # queryset = self.queryset.all().order_by(Lower('name'))
        # data = [entity.get_uri() for entity in queryset]
        # return Response(data)
        #
        return Response("Use just a username to get their PayId info if they are registered here on payid.rockhoward.com")

    def retrieve(self, request, name=None):
        user = get_object_or_404(self.queryset.filter(name__iexact=name))
        result = { "payId": user.get_uri(), "addresses": [] }
        for addr in user.get_crypto():
            result['addresses'].append( {
                "paymentNetwork": addr.paymentNetwork,
                "environment": addr.environment,
                "addressDetailsType": "CryptoAddressDetails",
                "addressDetails": {
                    "address": addr.address,
                    "tag": addr.tag
                    }
                })
        for addr in user.get_ach():
            result['addresses'].append( {
                "paymentNetwork": addr.paymentNetwork,
                "environment": addr.environment,
                "addressDetailsType": "ACHAddressDetails",
                "addressDetails": {
                    "accountNumber": addr.accountNumber,
                    "routingNumber": addr.routingNumber
                    }
                })

        return Response(result)

class LocalPayIdEntityViewSet(  mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = LocalPayIdEntity.objects.all()
    serializer_class = LocalPayIdEntitySerializer
    lookup_field = 'name'
    lookup_value_regex = '[\w\.\-\_\$]+' # FIXME -- Incomplete. Other chars plus some unicode are OK.
