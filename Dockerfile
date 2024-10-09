# Use a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container, it be used for data persistence 'volume'
WORKDIR /app

# Copy the requirements.txt file inside the docker container /app
COPY requirements.txt .

# Install dependencies. --no-cache-dir: Ensures that pip doesn't store downloaded files in the container, helping to reduce the size of the final image.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files from local machine currentdirectory to the container's directory (/app)
COPY . .

# This environment variable ensures that Python output is not buffered, meaning logs and print statements will be immediately visible in the container's output
ENV PYTHONUNBUFFERED 1

# Expose the port Django runs on (development)
EXPOSE 8000

# Optionally, set environment variables for production (e.g., DEBUG, DATABASE_URL)
# ENV DEBUG=False
# ENV DATABASE_URL=postgres://user:password@db:5432/mydatabase

# Run the Django development server (for development, change for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
