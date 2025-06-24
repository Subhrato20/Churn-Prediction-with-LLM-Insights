# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install fastapi uvicorn

# Copy project
COPY src/ ./src/

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8000"] 