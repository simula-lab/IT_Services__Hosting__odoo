# A Dockerfile to add pysaml2 to Odoo 1x
# pysaml2 is important for the the SAML module.
#
ARG ODOO_VERSION
FROM odoo:${ODOO_VERSION:-17}
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y pkg-config python3-dev build-essential
RUN apt-get install -y libxml2-dev libxmlsec1-dev libxmlsec1-openssl xmlsec1
RUN pip install pysaml2 xmlsec

# This is important to run the entrypoint.sh as the user odoo (and not root)
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
