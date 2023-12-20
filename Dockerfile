FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN python manage.py docker_superuser
RUN python manage.py load_initdata
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
