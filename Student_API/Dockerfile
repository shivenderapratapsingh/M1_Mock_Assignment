# Base image (python installed)
FROM python:3.11-slim

# create working directory inside container
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# expose port
EXPOSE 8000

# command to run API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]