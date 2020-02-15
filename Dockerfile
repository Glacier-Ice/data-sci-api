# We cannot use alpine since
# we need to call bash in entrypoint
FROM python:3.6

# Setup workdir
WORKDIR /data-sci-api

# Copy src files
COPY . .

# Install deps
RUN pip install -r requirements.txt

# Expose port 9000
EXPOSE 9000

# Start the server
ENTRYPOINT [ "bash", "start_server"]
