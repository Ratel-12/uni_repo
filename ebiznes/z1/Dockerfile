FROM ubuntu:22.04

ENV TZ=Europe/Warsaw
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install libssl-dev openssl wget gcc make \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev \
    unzip -y

RUN wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
    tar xzf Python-3.8.16.tgz && \
    cd Python-3.8.16 && \
    ./configure --prefix=/usr/local && \
    make && \
    make install

RUN apt-get update -y && \
    apt-get install openjdk-8-jdk -y

RUN apt-get update -y && \
    apt-get install kotlin -y

RUN wget https://services.gradle.org/distributions/gradle-8.0.2-bin.zip && \
    mkdir /opt/gradle && \
    unzip -d /opt/gradle gradle-8.0.2-bin.zip
    
ENV PATH=$PATH:/opt/gradle/gradle-8.0.2/bin

RUN useradd -ms /bin/bash luke_d
RUN adduser luke_d sudo

USER luke_d
RUN mkdir /home/luke_d/demo_hello/
WORKDIR /home/luke_d/demo_hello/

RUN gradle init --project-name demo_hello --package demo_hello --type java-application --dsl groovy --test-framework junit-jupiter --incubating

COPY build.gradle /home/luke_d/demo_hello/app/
RUN gradle

CMD ["gradle", "run"]

