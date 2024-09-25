# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app code
COPY . .

# Expose Flask app port
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]