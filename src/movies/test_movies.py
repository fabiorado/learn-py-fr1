import warnings
import pytest
import json
from pathlib import Path
from movies import DATA_FILE, Movie

# Arrange
@pytest.fixture
def setup_file():
    DATA_FILE = Path("../data/test_data.json").resolve()
    with open(DATA_FILE, "w") as f:
        json.dump([], f, indent=4)

@pytest.fixture
def movie(setup_file):
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

