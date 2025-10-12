import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("09:32:57 AM", self)
        self.timer = QTimer(self)
        self.initUI()
                                      
                                        
    def initUI(self):
        self.setWindowTitle("Personal Clock")
        # Set as tool window to hide from taskbar and stay on bottom (shows only on desktop background)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnBottomHint)
        self.setGeometry(1500, 400, 400, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())