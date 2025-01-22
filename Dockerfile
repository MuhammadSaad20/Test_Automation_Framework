# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to install dependencies
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port (optional for running tests)
# EXPOSE 5000

# Run the tests using pytest
CMD ["pytest", "src/tests/"]
