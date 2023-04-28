#!/usr/bin/env bash




# Clean CodeDeploy agent files for a fresh install

sudo rm -rf /home/ec2-user/install




# Install CodeDeploy agent

sudo yum -y update

sudo yum -y install ruby

sudo yum -y install wget

cd /home/ec2-user

wget https://aws-codedeploy-eu-north-1.s3.amazonaws.com/latest/install

sudo chmod +x ./install

sudo ./install auto




# Update OS & install Python3

sudo yum update -y

sudo yum install -y python3 python3-pip python3-devel

pip3 install --user --upgrade virtualenv

pip install Django

pip3 install django




# Delete app

sudo rm -rf /home/ec2-user/django-aws_cicd