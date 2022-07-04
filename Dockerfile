FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-project
COPY ./requirements.txt /django-project/requirements.txt
RUN pip install --no-cache-dir -r /django-project/requirements.txt
COPY . /django-project/