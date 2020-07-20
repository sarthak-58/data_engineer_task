FROM python:3
WORKDIR /usr/app/
COPY . .
ENV FILE_LOCATION=.
RUN pip install -r requirements.txt
CMD [ "python3", "app.py"]