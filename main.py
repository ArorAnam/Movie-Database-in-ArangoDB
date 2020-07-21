from arango import ArangoClient

# Initialize the Arango client
client = ArangoClient(hosts='https://localhost:8529')

# Connect to "_system" database as root user
# This returns an API wrapper for "_system" database
sys_db = client.db('system', username='root', password='naman02')

# Create a new database named "movies" id it does not exist
if not sys_db.has_database('movies'):
    sys_db.create_database('movies')

# Connect to the "movies" database as root user
# This return an API wrapper for "test" database
db = client.db('movies', username='root', password = 'naman02')

# Create a new collection
