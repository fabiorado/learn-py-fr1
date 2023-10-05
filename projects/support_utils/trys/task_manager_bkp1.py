import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame, QHBoxLayout
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Task:
    def __init__(self, name, start_date, end_date, message):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.message = message


class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.refresh)
        self.layout.addWidget(self.refresh_button)

        self.card_layout = QFrame()
        self.card_layout.setFrameShape(QFrame.StyledPanel)
        self.card_layout.setLayout(QVBoxLayout())

        self.layout.addWidget(self.card_layout)
        self.setLayout(self.layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(Qt.black)
        painter.setPen(pen)

        # Draw arrows between tasks here

    def refresh(self):
        # Load data from JSON file (Replace 'sample_data.json' with your actual file)
        with open('projects\support_utils\sample_data.json', 'r') as file:
            data = json.load(file)

        self.showTasks(data)

    def showTasks(self, data):
        # Clear existing cards
        card_layout = self.card_layout.layout()
        if card_layout is not None:
            while card_layout.count():
                item = card_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        for task_data in data:
            task = Task(task_data['Name'], task_data['StartDate'], task_data['EndDate'], task_data['Message'])
            self.addTaskCard(task)

        self.repaint()

    def addTaskCard(self, task):
        card = QFrame()
        card.setFrameShape(QFrame.Box)
        card_layout = QVBoxLayout()

        name_label = QLabel(f'Name: {task.name}')
        start_date_label = QLabel(f'Start Date: {task.start_date}')
        end_date_label = QLabel(f'End Date: {task.end_date}')
        message_label = QLabel(f'Message: {task.message}')

        card_layout.addWidget(name_label)
        card_layout.addWidget(start_date_label)
        card_layout.addWidget(end_date_label)
        card_layout.addWidget(message_label)

        card.setLayout(card_layout)

        self.card_layout.layout().addWidget(card)


def main():
    app = QApplication(sys.argv)
    ex = TaskManager()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
