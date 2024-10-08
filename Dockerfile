# Use a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Expose the port Django runs on (development)
EXPOSE 8000

# Optionally, set environment variables for production (e.g., DEBUG, DATABASE_URL)
# ENV DEBUG=False
# ENV DATABASE_URL=postgres://user:password@db:5432/mydatabase

# Run the Django development server (for development, change for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
