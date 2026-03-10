# Dockerfile
# Packages the FastAPI app and trained model into a container.
# This ensures the app runs identically in dev, staging, and production —
# a core DevOps principle called "environment parity".

# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer — speeds up rebuilds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Train the model at build time so it's baked into the container
RUN python model/train.py

# Expose the port FastAPI will run on
EXPOSE 8000

# Start the API server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]