# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables to ensure the output is sent directly to the terminal (helps with logs)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "CORE.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]