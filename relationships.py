from arango import ArangoClient

client = ArangoClient()

db = client.db('movies', username='root', password='naman02')

Movies = db.graph('Movies')

# Get the API wrapper for edge collection "acts_in"
if Movies.has_edge_definition('acts_in'):
    acts_in = Movies.edge_collection('acts_in')
else:
    acts_in = Movies.create_edge_definition(
        edge_collection='acts_in',
        from_vertex_collections=['actors'],
        to_vertex_collections=['films']
    )

# Get the API wrapper for edge collection "directs"
if Movies.has_edge_definition('directs'):
    directs = Movies.edge_collection('directs')
else:
    directs = Movies.create_edge_definition(
        edge_collection='directs',
        from_vertex_collections=['directors'],
        to_vertex_collections=['films']
    )

# Get the API wrapper for edge collection "hero"
if Movies.has_edge_definition('is_hero'):
    is_hero = Movies.edge_collection('is_hero')
else:
    directs = Movies.create_edge_definition(
        edge_collection='is_hero',
        from_vertex_collections=['actors'],
        to_vertex_collections=['hero']
    )

# Get the API wrapper for edge collection "heroine"
if Movies.has_edge_definition('is_heroine'):
    is_heroine = Movies.edge_collection('is_heroine')
else:
    directs = Movies.create_edge_definition(
        edge_collection='is_heroine',
        from_vertex_collections=['actors'],
        to_vertex_collections=['heroine']
    )

# Get the API wrapper for edge collection "villain"
if Movies.has_edge_definition('is_villain'):
    is_villain = Movies.edge_collection('is_villain')
else:
    directs = Movies.create_edge_definition(
        edge_collection='is_villain',
        from_vertex_collections=['actors'],
        to_vertex_collections=['villain']
    )

# print(Movies.edge_definitions())
