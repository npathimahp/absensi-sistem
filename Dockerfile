# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Set working directory dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Instal dependensi yang diperlukan, termasuk CMake untuk dlib
RUN apt-get update && \
    apt-get install -y cmake build-essential libopenblas-dev liblapack-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Menyalin sisa file aplikasi ke dalam container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose port yang digunakan oleh Flask (default 5000)
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["python", "run.py"]
