from logging import setLoggerClass
import sys
from types import resolve_bases
from PySide6 import QtCore, QtWidgets
from movies import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Add Movie")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Remove Movie(s)")

        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
    
    def populate_movies(self, reset=True):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        
        movie = Movie(movie_title)
        resultat = movie.add_to_movies()
        
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
        
        self.le_movieTitle.setText("")

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movie()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()

    sys.exit(app.exec())