# Build via docker:
# docker build -t ethereum-webserver '/dir/of/app'
# docker run -d --name eth-webserver -p 5000:5000 ethereum-webserver:latest

# Install Alpine Linux 3.10 with Python 3.8.0
FROM python:alpine3.10

# Update pip
RUN pip install --upgrade pip

# Make directory and set as working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies from requirements.txt
COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# Bundle Python app source
COPY ethereum.py /usr/src/app

# Expose port 5000 and run ethereum-webserver
EXPOSE 5000
CMD ["python", "/usr/src/app/ethereum.py"]