FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y software-properties-common

RUN add-apt-repository universe

RUN apt-get update \
    && apt-get install -y python3-pip

RUN apt-get update \
    && apt-get install -y --no-install-recommends mysql-server \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/GCP_to_MySQL_Download


COPY . /usr/src/app/GCP_to_MySQL_Download

WORKDIR /usr/src/app/GCP_to_MySQL_Download


RUN pip3 install -r requirements.txt

#RUN service mysql start
#RUN mysql < create_user.sql

EXPOSE 3306/tcp

ENTRYPOINT ["bash"]
