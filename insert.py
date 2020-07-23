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

# FILM #1
# --------------------------------------------------------------------------
films.insert({'_key': 'TheMatrix', 'title': 'The Matrix', 'released': 1999})

actors.insert({'_key': 'Keanu', 'name': 'Keanu Reaves', 'born': 1964})
actors.insert({'_key': 'Carrie', 'name': 'Carrie-Anne Moss', 'born': 1967})
actors.insert({'_key': "Hugo", 'name': 'Hugo Weaving', 'born': 1960})

directors.insert({'_key': 'Lana', 'name': 'Lana Wachowski', 'born': 1965})
directors.insert({'_key': 'Lily', 'name': 'Lily Wachowski', 'born': 1967})

hero.insert({'_key': 'matrix-hero', 'role': 'Neo'})
heroine.insert({'_key': 'matrix-heroine', 'role': 'Trinity'})
villain.insert({'_key': 'matrix-villain', 'role': 'Agent Smith'})

acts_in.insert({
    '_key': 'matrix-keanu',
    '_from': 'actors/Keanu',
    '_to': 'films/TheMatrix'
})

acts_in.insert({
    '_key': 'matrix-carrie',
    '_from': 'actors/Carrie',
    '_to': 'films/TheMatrix'
})

acts_in.insert({
    '_key': 'matrix-hugo',
    '_from': 'actors/Hugo',
    '_to': 'films/TheMatrix'
})

directs.insert({
    '_key': 'matrix-lana',
    '_from': 'directors/Lana',
    '_to': 'films/TheMatrix'
})

directs.insert({
    '_key': 'matrix-lily',
    '_from': 'directors/Lily',
    '_to': 'films/TheMatrix'
})

is_hero.insert({
    '_key': 'matrix-neo',
    '_from': 'actors/Keanu',
    '_to': 'hero/matrix-hero'
})

is_heroine.insert({
    '_key': 'matrix-trinity',
    '_from': 'actors/Carrie',
    '_to': 'heroine/matrix-heroine'
})

is_villain.insert({
    '_key': 'matrix-smith',
    '_from': 'actors/Hugo',
    '_to': 'villain/matrix-villain'
})


# # FILM #2
# # --------------------------------------------------------------------------
# films.insert({'_key': 'TheMatrixReloaded', 'title': 'The Matrix Reloaded', 'released': 2003})
#
# actors.insert({'_key': 'Keanu', 'name': 'Keanu Reaves', 'born': 1964})
# actors.insert({'_key': 'Carrie', 'name': 'Carrie-Anne Moss', 'born': 1967})
# actors.insert({'_key': "Hugo", 'name': 'Hugo Weaving', 'born': 1960})
#
# directors.insert({'_key': 'Lana', 'name': 'Lana Wachowski', 'born': 1965})
# directors.insert({'_key': 'Lily', 'name': 'Lily Wachowski', 'born': 1967})
#
# hero.insert({'_key': 'matrix-hero', 'role': 'Neo'})
# heroine.insert({'_key': 'matrix-heroine', 'role': 'Trinity'})
# villain.insert({'_key': 'matrix-villain', 'role': 'Agent Smith'})
#
# acts_in.insert({
#     '_key': 'matrix-keanu',
#     '_from': 'actors/Keanu',
#     '_to': 'films/TheMatrix'
# })
#
# acts_in.insert({
#     '_key': 'matrix-carrie',
#     '_from': 'actors/Carrie',
#     '_to': 'films/TheMatrix'
# })
#
# acts_in.insert({
#     '_key': 'matrix-hugo',
#     '_from': 'actors/Hugo',
#     '_to': 'films/TheMatrix'
# })
#
# directs.insert({
#     '_key': 'matrix-lana',
#     '_from': 'directors/Lana',
#     '_to': 'films/TheMatrix'
# })
#
# directs.insert({
#     '_key': 'matrix-lily',
#     '_from': 'directors/Lily',
#     '_to': 'films/TheMatrix'
# })
#
# is_hero.insert({
#     '_key': 'matrix-neo',
#     '_from': 'actors/Keanu',
#     '_to': 'hero/matrix-hero'
# })
#
# is_heroine.insert({
#     '_key': 'matrix-trinity',
#     '_from': 'actors/Carrie',
#     '_to': 'heroine/matrix-heroine'
# })
#
# is_villain.insert({
#     '_key': 'matrix-smith',
#     '_from': 'actors/Hugo',
#     '_to': 'villain/matrix-villain'
# })
