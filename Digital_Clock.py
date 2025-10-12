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
        self.setGeometry(1500, 400, 400, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 60px;"
                                      "font-family: Arial;"
                                      "color: #EAEAEA;"
                                      "background-color: #0A0F1F;")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())