FROM python:3.8

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080 5000

ENTRYPOINT ["python"]
CMD ["app.py"]

# CMD [ "sh", "-c", "python app.py"]