from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('movies', username='root', password='naman02')

# graph
Movies = db.graph('Movies')

# vertices
films = Movies.vertex_collection('films')
actors = Movies.vertex_collection('actors')
directors = Movies.vertex_collection('directors')
hero = Movies.vertex_collection('hero')
heroine = Movies.vertex_collection('heroine')
villain = Movies.vertex_collection('villain')

# edges
acts_in = Movies.edge_collection('acts_in')
directs = Movies.edge_collection('directs')
is_hero = Movies.edge_collection('is_hero')
is_heroine = Movies.edge_collection('is_heroine')
is_villain = Movies.edge_collection('is_villain')

# 1. actors, movie list
print("All actors ::")
for actor in actors:
    print(actor['name'], end=" ")

print("\nAll movies ::")
for film in films:
    print(film['title'], end=" ")

# 2. movie list of given 2 actors
actor_list = input("\nEnter actor first-names separated by commas : ")
actor_list = actor_list.split(',')

for actor in actor_list:
    start_vertex = 'actors/{}'.format(actor)

    # traverse from actor outbound
    movie_traversal = Movies.traverse(
        start_vertex=start_vertex,
        direction='outbound',
        strategy='bfs',
        edge_uniqueness='global',
        vertex_uniqueness='global'
    )

    vertices = movie_traversal['vertices']

    print("For {}, movies are :: ".format(actor), end=" ")
    for i in range(1, len(vertices)):
        if 'film' in vertices[i]['_id']:
            print(vertices[i]['title'], end=" ")

    print("\n")

# 3. movie list of given actor, director


# 4. list of directors the actor done movies with
actor = input("Enter actor name :: ")
start_vertex = 'actors/{}'.format(actor)

# traverse from actor outbound
movie_traversal = Movies.traverse(
    start_vertex=start_vertex,
    direction='outbound',
    strategy='bfs',
    edge_uniqueness='global',
    vertex_uniqueness='global'
)

vertices = movie_traversal['vertices']

film = []
for i in range(1, len(vertices)):
    if 'film' in vertices[i]['_id']:
        film.append(vertices[i]['_id'])

# traverse for  directors
for k in range(len(film)):
    start_vertex = film[k]
    dir_traversal = Movies.traverse(
        start_vertex=start_vertex,
        direction='inbound',
        strategy='bfs',
        edge_uniqueness='global',
        vertex_uniqueness='global'
    )

    vert = dir_traversal['vertices']

    for i in range(1, len(vert)):
        if 'directors' in vert[i]['_id']:
            print(vert[i]['name'], end=" ")

    print("\n")