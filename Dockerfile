# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    whois \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Train the model (this will create model/phishing_model.pkl)
RUN python -c "from phishing_detector.train_model import train_and_save_model; train_and_save_model()"

# Install the package in editable mode
RUN pip install -e .

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port (if you add a web interface later)
# EXPOSE 8000

# Set the entrypoint to the CLI tool
ENTRYPOINT ["phishing-detector"]

# Default command (can be overridden)
CMD ["--help"]