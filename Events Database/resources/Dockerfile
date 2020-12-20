FROM postgres:13-alpine

# Copy scripts to create tables at build-time
COPY ./create_tables.sql /docker-entrypoint-initdb.d/

ARG IMAGE_DESCRIPTION
LABEL Description=${IMAGE_DESCRIPTION}
