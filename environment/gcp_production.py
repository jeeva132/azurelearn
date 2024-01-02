import os

# Your new connection string
new_conn_str = "postgresql://findartist_user:7XOrSKhLhYl7P4Y7uctMlkU8qEfF7Lix@dpg-cma0q8md3nmc73b8undg-a.singapore-postgres.render.com/findartist"

# Parse the new connection string
parsed_url = urlparse(new_conn_str)

# Extract the components from the parsed URL
DB_CONNECTOR = parsed_url.scheme
DB_USER_NAME = parsed_url.username
DB_PASSWORD = parsed_url.password
DB_NAME = parsed_url.path.lstrip('/')
DB_PORT = parsed_url.port

# Create the new DATABASE_URI
DATABASE_URI = f"{DB_CONNECTOR}://{DB_USER_NAME}:{DB_PASSWORD}@/{DB_NAME}?unix_sock=/{DB_PORT}"
