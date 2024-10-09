# Use a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file inside the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Set environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run Gunicorn for production with 3 worker processes
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
