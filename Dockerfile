FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

#CMD ["python","main.py"]
CMD exec gunicorn --bind :8080 --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
