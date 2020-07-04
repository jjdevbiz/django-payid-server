from django.db import models
from django.conf import settings
from .utils import get_payid_uri

# FIXME : All of the max_length settings in models.py need to be checked versus the specs.

# FIXME : Do we need any additional logic in models.py to support JSON?

class LocalPayIdEntity(models.Model):
    # For payid entities managed on this server
    name = models.CharField(max_length=80)

    def get_uri(self):
        return get_payid_uri( self.name )

    def get_crypto(self, hide_if_not_show=True):
        queryset = CryptoAddress.objects.filter(entity=self)
        if hide_if_not_show is True:
            queryset = queryset.filter(show=True)
        return queryset

    def get_ach(self, hide_if_not_show=True):
        queryset = AchAddress.objects.filter(entity=self)
        if hide_if_not_show is True:
            queryset = queryset.filter(show=True)
        return queryset

    def __str__(self):
        return self.get_uri()

class AbstractAddress(models.Model):
    # A Local PayId Entity can have zero or more addresses.
    paymentNetwork = models.CharField(max_length = 8)
    environment = models.CharField(max_length = 12) # mainnet, testnet, etc.
    tag = models.CharField(max_length = 32, default='primary')
    show = models.BooleanField(default=True)
    entity = models.ForeignKey(LocalPayIdEntity, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class CryptoAddress(AbstractAddress):
    # CryptoAddressDetails is delivered in "addressDetails" field
    address = models.CharField(max_length = 128) # the public key for this crypto address (64 chars is typical)

    def __str__(self):
        return  ''.join((   "asset type: ", self.paymentNetwork, ", env: ", self.environment, \
                            ", tag: ", self.tag, ", addr: ", self.address))

class AchAddress(AbstractAddress):
    # AchAddressDetails is delivered in "addressDetails" field
    accountNumber = models.CharField(max_length=16) # 8 to 12 is most common in USA
    routingNumber = models.CharField(max_length=40) # IBAN is 34, ABA is most common in USA and is 9

    def __str__(self):
        return  ''.join((   "asset type: ", self.paymentNetwork, ", env: ", self.environment, ", tag: ", self.tag, \
                            ", routing: ", self.routingNumber, ", acct: ", self.accountNumber))
