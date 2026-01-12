#14.Names of movies:
movies = []
while True:
    movie = input("Enter movie name(type stop to end): ")
    if movie == "stop":
        break
    movies.append(movie)
print("List of the movies:", movies)
