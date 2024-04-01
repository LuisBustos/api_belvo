FROM ubuntu:latest

WORKDIR /finvero_api

COPY . /finvero_api
EXPOSE 8000


RUN apt update && apt-get install -y
RUN apt-get install mysql-server -y
RUN apt install systemctl -y
RUN apt install python3 -y
RUN apt install python3-pip -y 
RUN apt install python3-venv -y


CMD ["sh", "./init.sh"]