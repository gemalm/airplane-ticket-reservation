# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the backend directory into /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Expose the port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]