from django.contrib import admin
from django.conf import settings
from django import forms

from payid_validator import validate_payid, PayIdNotValidError
from .models import LocalPayIdEntity, CryptoAddress, AchAddress

class CryptoAddressInline(admin.TabularInline):
    model = CryptoAddress
    extra = 0

class AchAddressInline(admin.TabularInline):
    model = AchAddress
    extra = 0

class LocalPayIdEntityAdminForm(forms.ModelForm):
    def clean_name(self):
        # do something that validates your data
        payId = self.cleaned_data["name"] + "$" + settings.PAYID_URI_DOMAIN
        try:
            result = validate_payid(payId)
        except PayIdNotValidError as e:
            raise forms.ValidationError(str(e))
        return self.cleaned_data["name"]

@admin.register(LocalPayIdEntity)
class LocalPayIdEntityAdmin(admin.ModelAdmin):

    list_display = ("name", "_payid_URI", "_crypto_addresses", "_ach_addresses")

    inlines = [
        CryptoAddressInline,
        AchAddressInline
    ]

    form = LocalPayIdEntityAdminForm

    def _payid_URI(self, obj):
        return obj.get_uri()

    def _crypto_addresses(self, obj):
        return obj.get_crypto(hide_if_not_show=False).count()

    def _ach_addresses(self, obj):
        return obj.get_ach(hide_if_not_show=False).count()
