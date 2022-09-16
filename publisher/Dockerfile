FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["python"]
CMD ["publisher.py"]
