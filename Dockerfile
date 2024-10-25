ARG ODOO_VERSION

FROM odoo:${ODOO_VERSION:-17.0}
USER root
RUN apt-get update && apt-get upgrade -y

# Adding pysaml2 and depenedencies to support OCA/server_auth/auth_saml module.
#
RUN apt-get install -y pkg-config python3-dev build-essential git
RUN apt-get install -y libxml2-dev libxmlsec1-dev libxmlsec1-openssl xmlsec1 
RUN pip install pysaml2 xmlsec

RUN mkdir -p /mnt/apriori-addons

# Clone the odoomates/odooapps repository and copy all addons to /mnt/apriori-addons/
RUN git clone --branch ${ODOO_VERSION:-17.0} --depth 1 \
    https://github.com/odoomates/odooapps.git /tmp/repo && \
    find /tmp/repo -mindepth 1 -maxdepth 1 -type d -exec cp -r {} /mnt/apriori-addons/ \; && \
    rm -rf /tmp/repo

# Clone the OCA/server-auth repository and copy all addons to /mnt/apriori-addons/
RUN git clone --branch ${ODOO_VERSION:-17.0} --depth 1 \
    https://github.com/OCA/server-auth.git /tmp/repo && \
    cp -r /tmp/repo/auth_saml /mnt/apriori-addons/ && \ 
    rm -rf /tmp/repo

# Copy the base configurations to the image
COPY ./etc_odoo_odoo.conf /etc/odoo/odoo.conf

# This is important to run the entrypoint.sh as the user odoo (and not root)
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]

