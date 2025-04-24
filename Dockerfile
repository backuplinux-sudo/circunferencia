FROM python:IMAGEM_BASE

WORKDIR /app

COPY app.py .

ENTRYPOINT [ "python3", "app.py" ]
CMD [ "1" ]
