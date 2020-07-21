from arango import ArangoClient

# Initialize the Arango client
client = ArangoClient(hosts='http://localhost:8529')

# Connect to "_system" database as root user
# This returns an API wrapper for "_system" database
sys_db = client.db('_system', username='root', password='naman02')

# Create a new database named "movies" if it does not exist
if not sys_db.has_database('movies'):
    sys_db.create_database('movies')

# Connect to the "movies" database as root user
# This return an API wrapper for "test" database
db = client.db('movies', username='root', password='naman02')

# Create a new graph named "movies" if it dos not exist already
if db.has_graph('Movies'):
    Movies = db.graph('Movies')
else:
    Movies = db.create_graph('Movies')

# Retrieve various graph properties
# print(Movies.vertex_collections())
# print(Movies.edge_definitions())

# Create a new vertex collection named "films" to store all movies
if Movies.has_vertex_collection('films'):
    films = Movies.vertex_collection('films')
else:
    films = Movies.create_vertex_collection('films')

# Create a new vertex collection named "actors" to store all actors
if Movies.has_vertex_collection('actors'):
    actors = Movies.vertex_collection('actors')
else:
    actors = Movies.create_vertex_collection('actors')

# Create a new vertex collection named "directors" to store all movie directors
if Movies.has_vertex_collection('directors'):
    directors = Movies.vertex_collection('directors')
else:
    directors = Movies.create_vertex_collection('directors')

# Create a new vertex collection named "hero" to store all movie heros
if Movies.has_vertex_collection('hero'):
    hero = Movies.vertex_collection('hero')
else:
    hero = Movies.create_vertex_collection('hero')

# Create a new vertex collection named "heroine" to store all movie heroines
if Movies.has_vertex_collection('heroine'):
    heroine = Movies.vertex_collection('heroine')
else:
    heroine = Movies.create_vertex_collection('heroine')

# Create a new vertex collection named "directors" to store all movie villains
if Movies.has_vertex_collection('villain'):
    villain = Movies.vertex_collection('villain')
else:
    villain = Movies.create_vertex_collection('villain')