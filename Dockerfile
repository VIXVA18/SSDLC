# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src

# Ensure Python can import main.py from src/
ENV PYTHONPATH="/app/src"

# Set environment variable to avoid Python buffering output
ENV PYTHONUNBUFFERED=1

# Uncomment this CMD to run tests by default
# CMD ["bash", "-c", "coverage run -m unittest discover -s src -p 'test_*.py' && coverage report"]

# Default: run FastAPI app with Uvicorn on 0.0.0.0:8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
