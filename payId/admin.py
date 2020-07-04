from django.contrib import admin
from .models import LocalPayIdEntity, CryptoAddress, AchAddress

class CryptoAddressInline(admin.TabularInline):
    model = CryptoAddress
    extra = 0

class AchAddressInline(admin.TabularInline):
    model = AchAddress
    extra = 0

@admin.register(LocalPayIdEntity)
class LocalPayIdEntityAdmin(admin.ModelAdmin):

    list_display = ("name", "_payid_URI", "_crypto_addresses", "_ach_addresses")

    inlines = [
        CryptoAddressInline,
        AchAddressInline
    ]

    def _payid_URI(self, obj):
        return obj.get_uri()

    def _crypto_addresses(self, obj):
        return obj.get_crypto(hide_if_not_show=False).count()

    def _ach_addresses(self, obj):
        return obj.get_ach(hide_if_not_show=False).count()
