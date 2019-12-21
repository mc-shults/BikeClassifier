FROM ubuntu

WORKDIR /src/predict/
COPY . .

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install Pillow
RUN pip3 install tensorflow

CMD ["python3", "predict.py"]
