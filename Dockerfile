FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       default-libmysqlclient-dev gcc pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY req.pip /app/req.pip
RUN pip install --upgrade pip \
    && pip install -r req.pip

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

