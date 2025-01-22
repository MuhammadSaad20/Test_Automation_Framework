# Use a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to install dependencies
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files into the container
COPY . /app/

# Expose the required port (if applicable, for web apps)
EXPOSE 5000  
# Change the port if needed

# Set the default command to run your test suite (change this as needed)
CMD ["pytest", "src/tests/"]
