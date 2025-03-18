FROM python:3.9-alpine3.13
LABEL maintainer="bechir"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Python virtualenv
RUN apk add --no-cache \
    python3-dev \
    py3-pip \
    build-base \
    libffi-dev \
    musl-dev \
    gcc

# Copy the requirements file
COPY ./requirements.txt /tmp/requirements.txt
# Copy the developments requirments file 
COPY ./requirements.dev.txt  /tmp/requirements.dev.txt

# Create working directory
WORKDIR /app
COPY ./app /app

ARG DEV=false 
# Create a virtual environment and install dependencies
# requirements.txt
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
       then /py/bin/pip install -r /tmp/requirements.dev.txt ;\
       fi && \
    #manually installing django and RestFramework
    /py/bin/pip install "Django>=3.2.4,<3.3" "djangorestframework>=3.12.4,<3.13" && \  
    rm -rf /tmp 
# Set PATH to use the virtual environment
ENV PATH="/py/bin:$PATH"

# Create a non-root user for security
RUN adduser --disabled-password --no-create-home django-user

# Use the non-root user
USER django-user

# Expose the application port
EXPOSE 8001