# We Use an official Python runtime as a parent image
FROM python:3.10-slim
 
# install db libs
RUN apt-get update
RUN apt-get install -y default-mysql-client libmariadb-dev
RUN apt-get install -y libmariadb-dev-compat gcc gdal-bin libjpeg-dev
 
# install app libs
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
 
#falta agregar ordenes para acceder al mysql en docker compose
#falta agregar ordenes de creación de la base de datos original
#ordenes migrate

# Mounts the application code to the image
COPY . code
 
# establish workdir
WORKDIR /code
 
EXPOSE 8000 
 
# runs the development server
ENTRYPOINT ["python3","manage.py"]
CMD ["runserver","0.0.0.0:8000"]