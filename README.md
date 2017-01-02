# Django Tiler Service
A django based application which generates a map tiles using `gdal2tiles.py`. Requires a *TIFF* file as input when generating tiles. 

## Requirements
- Ubuntu 16.04
- Django
- GDAL
- PyGDAL

## Setup
1. Install system requirements:
  - `sudo apt-get install python-pip python-dev libpq-dev libgdal-dev libgdal1i python-gdal python-virtualenv`
2. Configure virtual environment:
 - Create virtual environemnt: `virtualenv env`
 - Activate virtual environment: `. env/bin/activate`
3. Install python libraries:
 - `pip install django`
4. Run the development server:
 - `sh run_dev.sh`

## Future Tasks
1. Create an interface for exporing the generated tiles.
2. Create a task queue for handling long running tasks (i.e tile generation)
3. Improve user interface of the layer viewer.
4. Add support to other raster formats.
5. Improve docs of the application.
