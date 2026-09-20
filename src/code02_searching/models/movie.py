import csv


class Movie:
    def __init__(
        self,
        no,
        id,
        title,
        original_title,
        original_language,
        popularity,
        release_date,
        vote_average,
        vote_count
    ):
        self.no = int(no)
        self.id = int(id)
        self.title = title
        self.original_title = original_title
        self.original_language = original_language
        self.popularity = float(popularity)
        self.release_date = release_date
        self.vote_average = float(vote_average)
        self.vote_count = int(vote_count)

    def __str__(self):
        return (
            f"Movie(id={self.id}, "
            f"title='{self.title}', "
            f"language='{self.original_language}', "
            f"rating={self.vote_average}, "
            f"votes={self.vote_count})"
        )
