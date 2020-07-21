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


print(Movies.edge_definitions())