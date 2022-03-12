# syntax=docker/dockerfile:1
FROM python:3.9.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /ImageSearcher/
COPY requirements.txt /ImageSearcher
RUN pip install -r requirements.txt
COPY . /ImageSearcher/