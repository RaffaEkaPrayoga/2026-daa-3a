class MovieCollection:
    def __init__(self, movies):
        self.movies = movies

    def show_all(self):
        for movie in self.movies:
            print(movie)

    def find_by_language(self, language):
        result = []

        for movie in self.movies:
            if movie.original_language == language:
                result.append(movie)

        return result

    def get_highest_rating(self):
        return max(
            self.movies,
            key=lambda movie: movie.vote_average
        )

