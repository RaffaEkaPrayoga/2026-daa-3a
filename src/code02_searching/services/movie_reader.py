import csv
from code02_searching.models.movie import Movie

class MovieReader:
    def __init__(self, filename):
        self.filename = filename

    def read_movies(self):
        movies = []

        with open(self.filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                movie = Movie(
                    row["no"],
                    row["id"],
                    row["title"],
                    row["original_title"],
                    row["original_language"],
                    row["popularity"],
                    row["release_date"],
                    row["vote_average"],
                    row["vote_count"]
                )

                movies.append(movie)

        return movies
