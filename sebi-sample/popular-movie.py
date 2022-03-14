movies = []

while True:
    movie = input()
    
    if movie == 'THE END':
        break

    movie = movie.split('#')
    movies.append( [movie[0], int(movie[1])] )


movies.sort(key = lambda x : (x[1], x[0]))

print(movies[0], movies[1])