import os
import json
import logging
import time

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, os.pardir, "data", "movies.json")

def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)
    
    movies = [Movie(movie_title) for movie_title in movies_title]
    
    return movies

class Movie:
    def __init__(self, title) -> None:
        self.title = title.title()

    def __str__(self):
        # pour que la classe puisse retourne autre chose que l'id de memoire
        return self.title 

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movie(self):
        movies = self._get_movies()
        
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'existe pas dans la liste.")
            return False

if __name__ == "__main__":
    m1 = Movie("Harry Potter")
    m2 = Movie("InsideOut")
    m1.add_to_movies()
    m2.add_to_movies()
    time.sleep(1)
    m2.remove_from_movie()

    print(get_movies())