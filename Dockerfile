# Use the official Python image as a base image
FROM python:3.8-slim

# Install required packages
RUN pip install selenium requests

# Download and install ChromeDriver
RUN apt-get update \
    && apt-get install -y unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Set the working directory
WORKDIR /app

# Copy your Selenium WebDriver script into the container
COPY test.py .

# Define the command to execute your script
CMD ["python", "test.py"]
