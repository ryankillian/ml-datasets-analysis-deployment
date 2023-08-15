# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
ADD requirements.txt /app/

# Install the Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and the model into the container
ADD . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run when the container starts
CMD ["python", "inference_script.py"]