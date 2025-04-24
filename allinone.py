from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QLabel, QSlider, QGridLayout
from PyQt5.QtCore import QRect, Qt
import sys

from logistic_model import perform_logistic_model
from age_structure import perform_age_structure_model
from predator import perform_predator
from saturation import perform_saturation

def make_slider(text, min, max, initial, parent, rect):
    label = QLabel(parent)
    label.setText(f'{text}: {initial}')
    label.setGeometry(QRect(rect.x(), rect.y() - 15, 300, 15))

    def onValueChanged(newValue):
        label.setText(f'{text}: {newValue}')

    slider = QSlider(parent)
    slider.setGeometry(rect)
    slider.setMinimum(min)
    slider.setMaximum(max)
    slider.setOrientation(Qt.Horizontal)
    slider.setInvertedAppearance(False)
    slider.setInvertedControls(False)
    slider.valueChanged.connect(onValueChanged)
    slider.setValue(initial)

    return slider

def predator_model_panel(parent):
    panel = QFrame(parent)
    panel.setGeometry(QRect(225, 15, 200, 180))
    panel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    title = QLabel(panel)
    title.setGeometry(QRect(5, 5, 150, 15))
    title.setText('Модель "Хищник-жертва"')

    param1Slider = make_slider("Альфа * 100", 1, 100, 80, panel, QRect(5, 40, 100, 10))
    param2Slider = make_slider("Бета * 100", 1, 100, 2, panel, QRect(5, 70, 100, 10))
    param3Slider = make_slider("Гамма * 100", 1, 100, 50, panel, QRect(5, 100, 100, 10))
    param4Slider = make_slider("Дельта * 100", 1, 100, 60, panel, QRect(5, 130, 100, 10))

    def onGo():
        perform_predator(
            param1Slider.value()/100.0, 
            param2Slider.value()/100.0, 
            param3Slider.value()/100.0,
            param4Slider.value()/100.0
        )

    go = QPushButton(panel)
    go.setGeometry(QRect(5, 150, 190, 25))
    go.setText("Построить")
    go.clicked.connect(onGo)

    return panel

def logistic_model_panel(parent):
    panel = QFrame(parent)
    panel.setGeometry(QRect(15, 15, 200, 150))
    panel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    title = QLabel(panel)
    title.setGeometry(QRect(5, 5, 150, 15))
    title.setText("Логистическая модель")

    param1Slider = make_slider("Начальная численность (N0)", 1, 100, 1, panel, QRect(5, 40, 100, 10))
    param2Slider = make_slider("Скорость роста (r*10)", 1, 50, 5, panel, QRect(5, 70, 100, 10))
    param3Slider = make_slider("Ёмкость среды (K)", 1, 300, 100, panel, QRect(5, 100, 100, 10))

    def onGo():
        perform_logistic_model(param1Slider.value(), param2Slider.value()/10.0, param3Slider.value())

    go = QPushButton(panel)
    go.setGeometry(QRect(5, 120, 190, 25))
    go.setText("Построить")
    go.clicked.connect(onGo)

    return panel

def saturation_model_panel(parent):
    panel = QFrame(parent)
    panel.setGeometry(QRect(225, 200, 200, 150))
    panel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    title = QLabel(panel)
    title.setGeometry(QRect(5, 5, 150, 15))
    title.setText("Учет насыщения")

    param1Slider = make_slider("Бета * 100", 1, 100, 2, panel, QRect(5, 40, 100, 10))
    param2Slider = make_slider("a * 10", 1, 10, 5, panel, QRect(5, 70, 100, 10))
    param3Slider = make_slider("b * 10", 1, 10, 1, panel, QRect(5, 100, 100, 10))

    def onGo():
        perform_saturation(param1Slider.value()/100.0, param2Slider.value()/10.0, param3Slider.value()/10.0)

    go = QPushButton(panel)
    go.setGeometry(QRect(5, 120, 190, 25))
    go.setText("Построить")
    go.clicked.connect(onGo)

    return panel

def age_structure_panel(parent):
    panel = QFrame(parent)
    panel.setGeometry(QRect(15, 175, 200, 240))
    panel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    title = QLabel(panel)
    title.setGeometry(QRect(5, 5, 200, 15))
    title.setText("Модель с возрастной структурой ")

    param1Slider = make_slider("Рождаемость молодых * 10", 0, 100, 0, panel, QRect(5, 40, 100, 10))
    param2Slider = make_slider("Рождаемость взрослых * 10", 0, 100, 12, panel, QRect(5, 70, 100, 10))
    param3Slider = make_slider("Рождаемость старых * 10", 0, 100, 5, panel, QRect(5, 100, 100, 10))
    param4Slider = make_slider("Выживаемость молодых %", 0, 100, 70, panel, QRect(5, 130, 100, 10))
    param5Slider = make_slider("Выживаемость взрослых %", 0, 100, 50, panel, QRect(5, 160, 100, 10))
    param6Slider = make_slider("Выживаемость старых %", 0, 100, 0, panel, QRect(5, 190, 100, 10))

    def onGo():
        perform_age_structure_model(
            param1Slider.value()/10.0, 
            param2Slider.value()/10.0, 
            param3Slider.value()/10.0,
            param4Slider.value()/100.0, 
            param5Slider.value()/100.0, 
            param6Slider.value()/100.0
        )

    go = QPushButton(panel)
    go.setGeometry(QRect(5, 210, 190, 25))
    go.setText("Построить")
    go.clicked.connect(onGo)

    return panel

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 430, 430)
    win.setWindowTitle("Программная реализация")

    logisticModelPanel = logistic_model_panel(win)
    ageModelPanel = age_structure_panel(win)
    predatorModelPanel = predator_model_panel(win)
    saturationModelPanel = saturation_model_panel(win)

    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()