FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y wget curl ca-certificates software-properties-common

# Installer Blender
RUN wget https://mirror.clarkson.edu/blender/release/Blender3.6/blender-3.6.0-linux-x64.tar.xz && \
    tar -xf blender-3.6.0-linux-x64.tar.xz && \
    mv blender-3.6.0-linux-x64 /opt/blender

ENV PATH="/opt/blender:${PATH}"

# Installer Python et dépendances
RUN apt-get install -y python3 python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copier le reste du code
COPY . .

EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
