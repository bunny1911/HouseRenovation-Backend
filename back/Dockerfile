# syntax=docker/dockerfile:1
FROM python:3.12-alpine

# Define work directory
WORKDIR /

# Copy files
COPY . .

# Update pip & install dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade -r requirements.txt

# Expose server port
EXPOSE 80

# Run ASGI
CMD ["uvicorn", "asgi:app", "--host", "localhost", "--port", "80"]
