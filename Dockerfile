FROM python:3.8

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .

WORKDIR .

RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
