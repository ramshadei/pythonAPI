# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables for the Flask app
ENV FLASK_APP=src/dbapi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5310

# Expose the port that Flask will run on
EXPOSE 5310

# Run the Flask app
CMD ["flask", "run"]
