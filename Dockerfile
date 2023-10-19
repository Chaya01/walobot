# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run your bot
CMD ["python", "walobotbot.py"]