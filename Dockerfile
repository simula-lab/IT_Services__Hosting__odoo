# A Dockerfile to add pysaml2 to Odoo 16
# pysaml2 is important for the the SAML module.
#
FROM odoo:16
USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl xmlsec1
RUN apt-get install -y python3.9-dev
RUN apt-get install -y build-essential
RUN pip install pysaml2 xmlsec

# This is important to run the entrypoint.sh as the user odoo (and not root)
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
