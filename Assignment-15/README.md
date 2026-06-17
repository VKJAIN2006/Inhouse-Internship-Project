# Dockerized Python Application

## Objective

This project demonstrates a Dockerized Python application using the official Python 3.12 Slim image.

The application displays:

- Current Python version
- Current Date and Time

---

## Project Structure

```text
Assignment-15
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── sample-output.png
```

Build Docker Image
docker build -t python-version-app .

Run Docker Container
docker run python-version-app