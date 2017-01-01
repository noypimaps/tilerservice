# Django Tiler Service
A django based application which generates a map tiles using `gdal2tiles.py`.

## Requirements
- Ubuntu 16.04
- Django
- GDAL
- PyGDAL
- Celery
- Redis

## Setup
1. Install system requirements:
  - sudo apt-get install python-pip python-dev libpq-dev libgdal-dev libgdal1i python-gdal aredis-server python-virtualenv
2. Configure virtual environment:
 - Create virtual environemnt: `virtualenv env`
 - Activate virtual environment: `. env/bin/activate`
3. Install python libraries:
 - pip install django celery redis
4. Run the development server:
 - python manage.py runserver
