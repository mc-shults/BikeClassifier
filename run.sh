#!/bin/bash

sudo docker image build -t predict:0.1.$1 .
sudo docker run predict:0.1.$1 
