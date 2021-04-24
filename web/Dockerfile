FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt


ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8000", "--workers=2", "webapp:get_app()"]