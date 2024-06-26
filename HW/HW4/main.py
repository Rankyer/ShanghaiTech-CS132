
import time
import sys
import DataBase

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor

from ui_to_py.control_UI import Ui_control

class control(QtWidgets.QMainWindow):
    def __init__(self, x, y, parent=None):
        super(control, self).__init__(parent)
        self.x=x
        self.y=y
        self.move(x, y)
        self.ui = Ui_control()
        self.ui.setupUi(self)

        self.ui.start.clicked.connect(self.start)
        self.ui.stop.clicked.connect(self.stop)
        self.show()

        self.running=0

    def start(self):
        try:
            red_time=int(self.ui.red.text())
            yellow_time=int(self.ui.yellow.text())
            green_time=int(self.ui.green.text())
        except:
            QMessageBox.information(self, "popup",  "All time settings must be positive integers!\n\n Please reset it 😔.")
            return

        if(red_time<=0 or yellow_time<=0 or green_time<=0):
            QMessageBox.information(self, "popup",  "All time settings must be positive integers!\n\n Please reset it 😔.")
        elif(yellow_time>red_time or yellow_time>green_time):
            QMessageBox.information(self, "popup",  "Sorry, the set time for the yellow light cannot exceed the time for the green or red light.\n\n Please reset it 😔.")
        elif(self.running==1):
            pass
        else:
            DataBase.red_time=red_time
            DataBase.yellow_time=yellow_time
            DataBase.green_time=green_time
            DataBase.start_clicked=1
            self.running=1
    def stop(self):
        if(DataBase.start_clicked!=0):
            DataBase.start_clicked=-1
            self.running=0

class TrafficLight(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Light")
        self.setGeometry(100, 200, 450, 300)
        self.light_sequence = ['red', 'green', 'yellow']
        self.initUI()
        self.initTimers()

    def initUI(self):
        self.lights = {
            'red': self.create_circle_pixmap(QColor(255, 0, 0)),
            'yellow': self.create_circle_pixmap(QColor(255, 255, 0)),
            'green': self.create_circle_pixmap(QColor(0, 255, 0)),
            'red_off': self.create_circle_pixmap(QColor(128, 0, 0)),
            'yellow_off': self.create_circle_pixmap(QColor(128, 128, 0)),
            'green_off': self.create_circle_pixmap(QColor(0, 128, 0))
        }

        self.light_labels = {
            'red': QLabel(self),
            'green': QLabel(self),
            'yellow': QLabel(self)
        }

        positions = {'red': 50, 'green': 180, 'yellow': 310}
        for key, label in self.light_labels.items():
            label.setGeometry(positions[key], 10, 100, 100)
            label.setPixmap(self.lights[f'{key}_off'])

        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(50, 200, 350, 80)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont('Arial', 20))

    def initTimers(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_traffic_light)
        self.check_status_timer = QTimer(self)
        self.check_status_timer.timeout.connect(self.check_status)
        self.check_status_timer.start(100)
        self.flashing_timer = QTimer(self)
        self.flashing_timer.timeout.connect(self.flash_yellow)
        self.flashing_timer.start(100)

    def create_circle_pixmap(self, color):
        pixmap = QPixmap(100, 100)
        pixmap.fill(QColor(0, 0, 0, 0))
        painter = QPainter(pixmap)
        painter.setBrush(color)
        painter.setPen(QColor(0, 0, 0, 0))
        painter.drawEllipse(0, 0, 100, 100)
        painter.end()
        return pixmap

    def update_traffic_light(self):
        if self.current_seconds > 1:
            self.current_seconds -= 1
            self.update_display()
            self.update_timer_label()
        else:
            self.advance_light()

    def advance_light(self):
        self.current_light_index = (self.current_light_index + 1) % len(self.light_sequence)
        self.current_light = self.light_sequence[self.current_light_index]
        self.current_seconds = getattr(DataBase, f"{self.current_light}_time")
        self.update_display()
        self.update_timer_label() 

    def check_status(self):
        if DataBase.start_clicked == 0:
            self.reset_lights()
        elif DataBase.start_clicked == 1 and not self.timer.isActive():
            self.start_lights()
        elif DataBase.start_clicked == -1 and not self.flashing_timer.isActive():
            self.reset_lights()
            self.start_flashing()

    def start_lights(self):
        self.flashing_timer.stop()
        self.current_light_index = -1
        self.advance_light()
        self.update_display()        # 立即更新灯光显示
        self.update_timer_label()    # 立即显示剩余秒数
        self.timer.start(1000)       # 然后每1000毫秒更新一次

    def reset_lights(self):
        self.timer.stop()
        self.flashing_timer.stop()
        for key, label in self.light_labels.items():
            label.setPixmap(self.lights[f'{key}_off'])
        self.timer_label.setText("")

    def start_flashing(self):
        self.timer.stop()  # Ensure no other timer is running
        self.flashing_timer.start(500)  # Start flashing yellow every 500ms

    def flash_yellow(self):
        # Toggle the state of the yellow light based on its current state
        current_pixmap = self.light_labels['yellow'].pixmap()
        if current_pixmap.toImage() == self.lights['yellow_off'].toImage():
            self.light_labels['yellow'].setPixmap(self.lights['yellow'])
            self.timer_label.setText("Flashing!")
        else:
            self.light_labels['yellow'].setPixmap(self.lights['yellow_off'])
            self.timer_label.setText("")

    def update_display(self):
        for key in self.light_labels:
            if key == self.current_light:
                self.light_labels[key].setPixmap(self.lights[key])
            else:
                self.light_labels[key].setPixmap(self.lights[f'{key}_off'])

    def update_timer_label(self):
        self.timer_label.setText(f"{self.current_seconds}s")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app1 = control(100,700)
    app1.show()

    light = TrafficLight()
    light.show()
    sys.exit(app.exec_())