# A Dockerfile to add pysaml2 to Odoo 15.
# pysaml2 is important for the the SAML module.
# 
FROM odoo:15
USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl
RUN apt-get install -y python3.9-dev
RUN apt-get install -y build-essential
RUN pip install xmlsec
RUN pip install pysaml2
