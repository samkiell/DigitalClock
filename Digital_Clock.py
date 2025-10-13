import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint
from PyQt5.QtGui import QMouseEvent

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("09:32:57 AM", self)
        self.title_label = QLabel("Personal Clock", self)
        self.timer = QTimer(self)
        self.drag_position = QPoint()
        self.initUI()


    def initUI(self):
        # Set as frameless tool window to hide from taskbar and stay on bottom
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint)
        self.setGeometry(1500, 400, 400, 120)

        # Set widget background to match label
        self.setStyleSheet("background-color: #0A0F1F;")

        vbox = QVBoxLayout()
        # Custom title bar
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 14px;"
                                       "font-family: Arial;"
                                       "color: #EAEAEA;"
                                       "background-color: #0A0F1F;"
                                       "padding: 5px;")
        self.title_label.setFixedHeight(25)
        vbox.addWidget(self.title_label)

        # Time label
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        # Remove margins to eliminate white borders
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 60px;"
                                      "font-family: Arial;"
                                      "color: #EAEAEA;"
                                      "background-color: #0A0F1F;")

        # Connect timer to update time every second
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()  # Initial update

    def update_time(self):
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss AP"))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())