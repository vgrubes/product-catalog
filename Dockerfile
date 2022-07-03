FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-project
COPY requirements.txt /django-project/
RUN pip install -r requirements.txt
COPY . /django-project/