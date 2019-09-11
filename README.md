# Django Weather Service

This API collects data from multiple services to calculate an average for the current temperature
in a given latitude/longitude

## Available services

So far the following services have been implemented:

 * NOAA
 * Accuweather
 * Weather.com

## Usage

Data can be fetched for a given latitude with the following URL:
`/api/<latitude>/<longitude>/`. Services can be selected with the `sources` parameter, as a comma
separated list.

Example:
`GET /api/44/33/?sources=noaa,accuweather`

## Installation

Most environment settings can be configured by environment variables:

 * `DEBUG`: when set to true, enables django's debug mode. Defaults to `false`
 * `ALLOWED_HOSTS`: comma separated list of domains allowed for the application. Defaults to an empty list
 * `WEATHER_SERVICE_URL`: Full URL to the service that collects weather sources. Defaults to `http://localhost:5000`

### From source:

Setup a virtualenv for the project's dependencies `python3 -m venv env && source env/bin/activate && pip install -r requirements.txt`

### From Docker:

A simple Dockerfile is provided to containerize the runtime environment. A generic deploy would
consist of building the image and running it on an exposed port:

`docker build . -t django-weather-service && docker run -d -p 80:8000 django-weather-service`

**NOTE**: if the service is run with Docker, services that bind to `localhost` won't be accessible by the container
