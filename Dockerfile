FROM python:3.8

COPY ./app /app
WORKDIR /app

# Установка пакетов из интернета
# RUN pip install -r requirements.txt

# Установка из заранее скаченых пакетов
# установить PIP
RUN pip install pkg/docker/pip-21.3.1-py3-none-any.whl
# установить список пакетов из каталога
RUN pip install --no-index --find-links app/pkg/docker -r requirements.txt

EXPOSE 8080 5000

ENTRYPOINT ["python"]
CMD ["app.py"]cd /

# CMD [ "sh", "-c", "python app.py"]