# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /backand_payments
COPY requirements.txt /backand_payments/
RUN pip install -r requirements.txt
COPY . /backand_payments/