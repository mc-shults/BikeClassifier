#!/bin/bash

sudo docker image build -t predict:0.1.$1 .
sudo docker run --detach --restart on-failure --name predict predict:0.1.$1 
