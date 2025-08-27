FROM python:3.9-alpine

WORKDIR /app
COPY . .
ENV PBR_VERSION=1.0
RUN pip install .
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
