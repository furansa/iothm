FROM python:3.8-slim

WORKDIR /api

COPY ./Pipfile /api/

ARG IMAGE_DESCRIPTION
LABEL Description=${IMAGE_DESCRIPTION}

# Update the system and install required packages
ARG PIP_OPTIONS
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl && apt-get clean && \
pip3 install --upgrade pip && pip3 install pipenv && pipenv install ${PIP_OPTIONS}

ENTRYPOINT ["/tmp/entrypoint.sh"]
