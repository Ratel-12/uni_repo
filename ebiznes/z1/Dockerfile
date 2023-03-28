FROM ubuntu:22.04

ENV TZ=Europe/Warsaw
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt-get install -y python3.8 python3.8-dev python3-pip 
RUN apt-get clean -y
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
RUN python --version

RUN apt-get update -y
RUN apt-get install openjdk-8-jdk -y
RUN java -version

RUN apt-get update -y
RUN apt-get install -y curl zip unzip
RUN curl -s "https://get.sdkman.io" | bash
RUN echo "source \"/root/.sdkman/bin/sdkman-init.sh\"" >> /root/.bashrc
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk version"
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install kotlin"
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && kotlin -version"

RUN apt-get update -y
RUN apt-get install gradle -y
RUN gradle -version

RUN useradd -ms /bin/bash luke_d
RUN adduser luke_d sudo
USER luke_d

RUN mkdir /home/luke_d/demo_hello
WORKDIR /home/luke_d/demo_hello
ADD demo_hello .
RUN gradle build

CMD gradle run

