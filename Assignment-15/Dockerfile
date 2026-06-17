FROM python:3.12-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt

# Run application
CMD ["python", "app.py"]