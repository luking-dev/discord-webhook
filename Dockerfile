FROM python:3.9-slim


# Copy the Python scripts into the container
COPY . /.

# Install required Python packages
RUN pip install -r requirements.txt

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint to run the script
ENTRYPOINT ["/entrypoint.sh"]