# Use the cxpy image as the base
FROM cxpy

# Copy your Flask application code into the container
COPY . /app

# Install Flask and any other dependencies
RUN pip install Flask

# Expose the port your Flask app runs on
EXPOSE 5000

# Set the working directory
WORKDIR /app

# Command to run the Flask app
CMD ["python3", "app.py"]
