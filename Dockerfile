FROM cicirello/pyaction:latest

WORKDIR /app
COPY . .
RUN pip install .
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
