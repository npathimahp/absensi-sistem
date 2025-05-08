FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libgl1

COPY requirements.txt requirements.txt

# Tambahkan file serviceAccountKey.json ke image
COPY serviceAccountKey.json /app/serviceAccountKey.json

COPY run.py .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
