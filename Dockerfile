FROM ubuntu:24.04

WORKDIR /usr/src/mergebot
RUN chmod 777 /usr/src/mergebot

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install apt-utils -y \ 
    && apt-get install -y python3-full python3-pip git wget curl pv jq ffmpeg neofetch mediainfo \
    && apt-get clean
    FROM python:3.8-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Set the entry point for your application
CMD ["python", "your_script.py"]

## To enable rclone upload, uncommnet the following line; 
# RUN curl https://rclone.org/install.sh | bash

RUN python3 -m venv venv && chmod +x venv/bin/python

COPY requirements.txt .
RUN venv/bin/python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn app:app & python3 bot.py
