# django-payid-server

A Django-based PayId reference server.

This version targets version 1.0 of the PayId standard. This includes:

- URI spec: [RFCS draftfuelling-payid-uri-01](https://github.com/payid-org/rfcs/blob/master/dist/spec/payid-uri.txt)
- Whitepaper [PayID Protocol](https://payid.org/whitepaper.pdf)

### Caveats

This is a pre-alpha release. It has no packaging and is missing some configuration info.

### Limitations

This version of the reference server only handles the primary GET endpoint.
To invoke it do a GET on the relative address of "/some_name/" where some_name is the
PayId account name (that is does not include the last '$' and the subsequent domain string.)

### Usage

You need to create a file called secrets.py and place it in your main directory (i.e., alongside 'manage.py')
It must include your DJANGO_SECRET_KEY.

(Later we will probably be adding other security info to this file.)

Manage the domain of your server via the PAYID_URI_DOMAIN setting in the settings file.

### Next Steps

No validity checking is done for the PayId at this time.
(Next we will add support for validity checking using logic from the python-payid-validator repo.)

The private (aka 'admin') CRUD APIs at /users/ will be added soon. Note that these APIs are optional. 
For now you can use the Django admin to enter payID account names and addresses into your database.
