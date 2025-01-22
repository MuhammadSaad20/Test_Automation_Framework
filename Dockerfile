# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to install dependencies
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app (including src folder) to the container
COPY . /app/


# Set the environment variable to make the src directory available for imports
ENV PYTHONPATH=/app/src

# Run the tests
CMD ["pytest", "src/tests/"]
