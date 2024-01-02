import os
from urllib.parse import urlparse

# Your new connection string
conn_str = "postgres://findartist_user:7XOrSKhLhYl7P4Y7uctMlkU8qEfF7Lix@dpg-cma0q8md3nmc73b8undg-a.singapore-postgres.render.com/findartist"

# Parse the connection string
parsed_url = urlparse(conn_str)

# Extract the components from the parsed URL
DB_USER = parsed_url.username
DB_PASSWORD = parsed_url.password
DB_HOST = parsed_url.hostname
DB_PORT = parsed_url.port
DB_NAME = parsed_url.path.lstrip('/')

# Create the new DATABASE_URI
DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
