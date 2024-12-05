# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the requirements file (create one if you have dependencies)
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]