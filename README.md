# Sentiment Analysis API

## Overview

This project demonstrates how to serve a sentiment analysis model via a REST API using Flask and integrate it with a PostgreSQL database. The goal is to exercise the deployment of machine learning models in a production-like environment, highlighting key skills in API development, containerization, and database integration.

## Key Features

- **Sentiment Analysis Model**: Utilized the VADER (Valence Aware Dictionary and Sentiment Reasoner) for sentiment analysis, providing real-time sentiment scoring of input text.
  
- **API Development**: Developed a simple Flask application to expose the sentiment analysis model via an API endpoint, allowing users to submit text and receive sentiment scores.

- **Containerization**: Created a Dockerfile to containerize the Flask application, ensuring that all dependencies (such as Python, Flask, and required libraries) are packaged together for easy deployment.

- **Database Integration**: Integrated a PostgreSQL database to store API logs, including timestamps and input text. This allows for tracking and analyzing API usage.

- **Docker Compose**: Utilized Docker Compose to manage multi-container applications, facilitating seamless communication between the Flask API and PostgreSQL database.

## Technologies Used

- **Python**: For implementing the sentiment analysis model and API.
- **Flask**: To create the RESTful API for serving the sentiment analysis functionality.
- **Docker**: For containerizing the application and ensuring consistent environments across different deployments.
- **Docker Compose**: To manage the multi-container setup, including the Flask application and PostgreSQL database.
- **PostgreSQL**: For database management and storage of API logs.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/AliakbarMehdizadeh/docker-api-sentiment.git
   cd docker-api-sentiment
2. Build and start the application with Docker Compose:
   ```bash
   docker-compose up --build
4. Access the API at `http://localhost:5001` and send requests to analyze sentiment:
   ```bash
   curl -X POST http://localhost:5001/sentiment -H "Content-Type: application/json" -d '{"text": "I love programming!"}'

## Future Enhancements:

- Implement authentication for API access.
- Add more advanced sentiment analysis models (e.g., fine-tuned transformer models).
- Enhance logging and monitoring of API usage.

