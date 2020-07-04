# from django.core.validators import validate_email
from django.conf import settings

def get_payid_uri( name ):
    return ''.join((name.lower(), '$', settings.PAYID_URI_DOMAIN))
