# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Create a virtual environment using python -m venv
RUN python -m venv env

# Activate the virtual environment and install the required Python packages
RUN . env/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5001 for the Flask application
EXPOSE 5001

# Command to run the Flask application using the virtual environment's Python
CMD ["env/bin/python", "app.py"]
