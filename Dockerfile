FROM python:3-alpine

# init
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/

# setup
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install -r requirements.txt

# prep
ENV PYTHONUNBUFFERED 1
ENV DEBUG=true
ENV WEATHER_SERVICE_URL="http://localhost:5000"
ENV ALLOWED_HOSTS="localhost,127.0.0.1"
COPY . /www/

WORKDIR /www/testusa

EXPOSE 8000/tcp

CMD ["gunicorn", "-b", "0.0.0.0:8000", "testusa.wsgi"]
