FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends mysql-server \
    && rm -rm /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/GCP_to_MySQL_Download

COPY . /usr/src/app/GCP_to_MySQL_Download

WORKDIR /usr/src/app/GCP_to_MySQL_Download

pip install -r requirements.txt

CMD ["bash"]