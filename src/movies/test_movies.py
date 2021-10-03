import warnings
import pytest
from movies import Movie

# Arrange
@pytest.fixture
def movie():
    return Movie(title="It")

# Assert
def test_add_movie(movie):
    movie.add_to_movies()
    assert "It" in movie._get_movies()

def test_warning():
    with pytest.warns(UserWarning, match='Le film It est déjà enregistré.'):
        warnings.warn("Le film It est déjà enregistré.", UserWarning)

def test_remove_movie(movie):
    movie.remove_from_movie()
    assert "It" not in movie._get_movies()

# A ... Clean

