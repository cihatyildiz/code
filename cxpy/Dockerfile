# Use Ubuntu as the base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update \
    && apt-get install -y python3.12 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Set the Python version as default
RUN ln -sf /usr/bin/python3.12 /usr/bin/python3

# Set up a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install pip packages
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Default command to run when the container starts
CMD ["python3"]
