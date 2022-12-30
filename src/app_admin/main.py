from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent

# Build a desktop app to execute scripts
class belt_app(QWidget):
    '''
    Top: standard menu + control buttons (start, stop, kill ...)
    Left: dinamic menu that shows the list of scripts
    Center: black cmd screen with the output
    Buton: status
    '''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Belt App")
        self.setup_ui()
    
    def setup_ui(self):
        pass

    def setup_connections(self):
        pass



if __name__ == "__main__":
    pass
    


