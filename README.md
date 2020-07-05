# django-payid-server

A Django-based PayId reference server.

This version targets version 1.0 of the PayId standard. This includes:

- URI spec: [RFCS draftfuelling-payid-uri-01](https://github.com/payid-org/rfcs/blob/master/dist/spec/payid-uri.txt)
- Whitepaper [PayID Protocol](https://payid.org/whitepaper.pdf)

### Caveats

This is an alpha release.

This django app depend on the python-payid-validator package.

### Limitations

This version of the reference server only handles the primary GET endpoint.
To invoke it do a GET on the relative address of "/some_name/" where some_name is the
PayId account name (that is does not include the last '$' and the subsequent domain string.)
Limited validation checking is performed at this time.

### Usage

You need to create a file called secrets.py and place it in your main directory (i.e., alongside 'manage.py')
It must include your DJANGO_SECRET_KEY.

(Later we will probably be adding other security info to this file.)

Manage the domain of your server via the PAYID_URI_DOMAIN setting in the settings file.

### Next Steps

The private (aka 'admin') CRUD APIs at /users/ will be added next. Note that these APIs are optional. 
You can use your own custom logic instead however this logic needs to be extra secure so that only
trusted sources can change the local database of PayIds and their associated addresses.
(Eventually this app will add some of the optional Verification logic specified by the PayId Protocol.)

Right now you can use the Django admin to enter payID account names and addresses into your database.
