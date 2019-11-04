# Build via docker:
# docker build -t ethereum-webserver .
# docker run -d --name ethereum-webserver -p 80:80 ethereum-webserver:latest

# Install Python 3.7.0/Flask, uWSGI, Nginx
FROM tiangolo/uwsgi-nginx-flask:python3.7

#Set custom listen port
#ENV LISTEN_PORT 8080

# Update pip
RUN pip install --upgrade pip

# Make directory and set as working directory
RUN mkdir -p /app
WORKDIR /app

# Install app dependencies from requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy uwsgi.ini config file
COPY uwsgi.ini /app

# Bundle Python app source
COPY ethereum.py /app

# Expose port 80 or custom port
EXPOSE 80
