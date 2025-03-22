FROM python:3.11.10-alpine3.20

WORKDIR /app

COPY app.py .

ENTRYPOINT [ "python3", "app.py" ]
CMD [ "1" ]
