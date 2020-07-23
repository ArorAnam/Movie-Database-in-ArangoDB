from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('movies', username='root', password='naman02')

# graph
Movies = db.graph('Movies')

# # vertices
# films = Movies.vertex_collection('films')
# actors = Movies.vertex_collection('actors')
# directors = Movies.vertex_collection('directors')
# hero = Movies.vertex_collection('hero')
# heroine = Movies.vertex_collection('heroine')
# villain = Movies.vertex_collection('villain')
#
# # edges
# acts_in = Movies.edge_collection('acts_in')
# directs = Movies.edge_collection('directs')
# is_hero = Movies.edge_collection('is_hero')
# is_heroine = Movies.edge_collection('is_heroine')
# is_villain = Movies.edge_collection('is_villain')

# traverse from Keanu outbound
trv = Movies.traverse(
    start_vertex='actors/Keanu',
    direction='outbound',
    strategy='bfs',
    edge_uniqueness='global',
    vertex_uniqueness='global'
)

vertices = trv['vertices']

for i in range(1, len(vertices)):
    if 'film' in vertices[i]['_id']:
        print(vertices[i]['title'])



