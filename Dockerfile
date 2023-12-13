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
COPY init_data.sql /app
RUN python manage.py dbshell < init_data.sql
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin', 'admin')" | python manage.py shell
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
