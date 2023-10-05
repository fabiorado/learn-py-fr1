import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QRectF, QPointF


class Task:
    def __init__(self, name, start_date, end_date, message):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.message = message


class Arrow:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos


class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.refresh)
        self.layout.addWidget(self.refresh_button)

        self.graphics_view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

        self.tasks = []
        self.arrows = []

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(Qt.black)
        painter.setPen(pen)

        for arrow in self.arrows:
            painter.drawLine(arrow.start_pos, arrow.end_pos)

    def refresh(self):
        # Load data from JSON file (Replace 'sample_data.json' with your actual file)
        with open('projects\support_utils\sample_data.json', 'r') as file:
            data = json.load(file)

        self.showTasks(data)

    def showTasks(self, data):
        self.tasks = []

        for task_data in data:
            task = Task(task_data['Name'], task_data['StartDate'], task_data['EndDate'], task_data['Message'])
            self.tasks.append(task)

        self.drawArrows()

    def drawArrows(self):
        self.arrows = []

        for i in range(len(self.tasks)-1):
            start_task = self.tasks[i]
            end_task = self.tasks[i+1]

            start_pos = QPointF(50, i*150 + 100)
            end_pos = QPointF(250, (i+1)*150 + 100)

            self.arrows.append(Arrow(start_pos, end_pos))

        self.scene.setSceneRect(QRectF(0, 0, 300, len(self.tasks)*150))
        self.graphics_view.setSceneRect(QRectF(0, 0, 300, len(self.tasks)*150))
        self.graphics_view.update()

    def mousePressEvent(self, event):
        item = self.graphics_view.itemAt(event.pos())
        if item:
            item.setFlag(QGraphicsItem.ItemIsMovable)

    def mouseReleaseEvent(self, event):
        item = self.graphics_view.itemAt(event.pos())
        if item:
            item.setFlag(QGraphicsItem.ItemIsMovable, False)


def main():
    app = QApplication(sys.argv)
    ex = TaskManager()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
