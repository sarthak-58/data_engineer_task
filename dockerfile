FROM python:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_DEFAULT_REGION=us-east-1
ENV FILE_LOCATION=.
WORKDIR /usr/app/
COPY . .
RUN \
    apt update && \
        apt-get install awscli --yes
RUN pip install -r requirements.txt
CMD [ "python3", "app.py"]
